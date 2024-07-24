from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-me/', views.contact, name='contact'),  # updated path
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
]
