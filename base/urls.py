from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact-us/', views.Contact, name='contact'),
    path('about-us/', views.About, name='about'),
    path('storage-service/', views.Storage, name='storage'),
    path('rental-service/', views.Rental, name='rental'),
    path('agro-store/', views.AgroStore, name='store'),
    path('sitemap/', views.Sitemap, name='sitemap')
]
