from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact-us/', views.Contact, name='contact'),
    path('about-us/', views.About, name='about'),
]
