from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import URL, Click

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    # Admin configuration for URL model
    
    # Fields to display in list view
    list_display = [
        'short_code',
        'created_by',
        'clicks',
        'created_at',
        'expiration_date',
        'is_expired',
    ]
    
    # Searchable fields
    search_fields = [
        'original_url',
        'short_code',
        'created_by__username',
        'created_by__email'
    ]
    
    # Filters
    list_filter = [
        'created_at',
        'created_by',
    ]
    
    # Read-only fields
    readonly_fields = [
        'short_code',
        'created_at',
        'clicks',
    ]
    
    # Fieldsets for edit page
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'original_url',
                'short_code',
                'created_by'
            )
        }),
        ('Statistics & Info', {
            'fields': (
                'clicks',
                'created_at',
            )
        }),
        ('Advanced Settings', {
            'fields': (
                'expiration_date',
            ),
            'classes': ('collapse',)
        }),
    )
    
    # Default ordering
    ordering = ['-created_at']
    
    # Items per page
    list_per_page = 25
    
    def is_expired(self, obj):
        # Display expiration status
        if obj.expiration_date and obj.expiration_date < timezone.now():
            return format_html('<span style="color: red;">⛔ Expired</span>')
        return format_html('<span style="color: green;">✅ Active</span>')
    is_expired.short_description = 'Status'
    
    def get_queryset(self, request):
        # Optimize queries with prefetch_related
        return super().get_queryset(request).select_related('created_by')

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    # Admin configuration for Click model
    
    # Fields to display in list view
    list_display = [
        'url_link',
        'clicked_at',
        'ip_address',
        'click_info'
    ]
    
    # Read-only fields
    readonly_fields = [
        'url',
        'clicked_at',
        'ip_address',
        'user_agent',
        'click_info'
    ]
    
    # Filters
    list_filter = [
        'clicked_at',
        'ip_address',
        'url__short_code'
    ]
    
    # Search fields
    search_fields = [
        'ip_address',
        'user_agent',
        'url__original_url',
        'url__short_code'
    ]
    
    # Ordering
    ordering = ['-clicked_at']
    
    # Items per page
    list_per_page = 50
    
    def url_link(self, obj):
        """Display link to related URL"""
        return format_html(
            '<a href="{}">{}</a>',
            f'/admin/shortener/url/{obj.url.id}/change/',
            obj.url.short_code
        )
    url_link.short_description = 'Short URL'
    
    def click_info(self, obj):
        """Display complete click information"""
        return format_html("""
            <div style="background: #f8f9fa; padding: 15px; border-radius: 5px;">
                <strong>Click Information:</strong><br>
                <strong>IP:</strong> {}<br>
                <strong>Time:</strong> {}<br>
                <strong>User Agent:</strong> {}<br>
                <strong>Related URL:</strong> {}<br>
                <strong>Original URL:</strong> {}
            </div>
        """, obj.ip_address, obj.clicked_at, obj.user_agent, 
           obj.url.short_code, obj.url.original_url)
    click_info.short_description = 'Click Details'

# Admin site settings
admin.site.site_header = 'URL Shortener Administration'
admin.site.site_title = 'URL Shortener Service'
admin.site.index_title = 'URL & Analytics Management'