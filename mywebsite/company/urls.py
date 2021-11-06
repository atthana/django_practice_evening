from django.urls import path

# from .views import AboutUs, Home

from .views import *

urlpatterns = [
    path('', Home, name='home-page'),  # http://localhost:8000/
    path('about/', AboutUs, name='about-page'),  # http://localhost:8000/about/
    path('contact/', ContactUs, name='contact-page'),
    
]