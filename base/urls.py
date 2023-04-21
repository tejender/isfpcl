from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact-us/', views.Contact, name='contact'),
    path('about-us/', views.About, name='about'),
    path('storage-service/', views.Storage, name='storage'),
    path('rental-service/', views.Rental, name='rental'),
    path('agro-store/', views.AgroStore, name='store'),
    path('sitemap/', views.Sitemap, name='sitemap'),
    path('sitemap.xml/', TemplateView.as_view(template_name='base/sitemap.xml',content_type='text/xml') ),

        
]
