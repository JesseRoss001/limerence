# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('other-services/', views.other_services, name='other_services'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
]
