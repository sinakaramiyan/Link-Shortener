from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<str:short_code>/', views.RedirectView.as_view(), name='RedirectView'),
    path('links', views.UserLinkView.as_view(), name='UserLinks'),
]