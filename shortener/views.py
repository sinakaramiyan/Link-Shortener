from django.views import generic
from .models import URL, Click
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

class HomeView(generic.TemplateView):
    template_name = "home/index.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        original_url = request.POST.get('original_url')
        exist_url = URL.objects.filter(original_url=original_url).exists()
        if not exist_url:
            # Create URL object
            url_obj = URL(
                original_url=original_url,
                created_by=request.user
            )
            url_obj.save()
            
            # Add the short URL to context
            context['short_url'] = f"{request.build_absolute_uri('/')}{url_obj.short_code}"
            context['original_url'] = original_url
            
            return self.render_to_response(context)
        else:
            context['exist_url'] = True
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initialize empty context for GET requests
        context.setdefault('short_url', None)
        context.setdefault('original_url', None)
        context.setdefault('exist_url', None)
        return context
    
class RedirectView(generic.View):
    # Redirect to main URL
    
    def get(self, request, short_code):
        url = get_object_or_404(URL, short_code=short_code)
        
        # Check expiration day
        if url.expiration_date and url.expiration_date < timezone.now():
            raise Http404("این لینک منقضی شده است")
        
        # INcrease click number
        url.clicks += 1
        url.save()
        
        # save information
        Click.objects.create(
            url=url,
            ip_address=self.get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )
        
        return HttpResponseRedirect(url.original_url)
    
    def get_client_ip(self, request):
        # Recieve user IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
class UserLinkView(generic.TemplateView):
    model = URL
    template_name = 'link_list/user_links.html'
    context_object_name = 'url'
    
    def get_queryset(self):
        return URL.objects.filter(created_by=self.request.user).order_by('created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_links'] = self.get_queryset
        return context
