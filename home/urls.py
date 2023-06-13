from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_pfsa, name='about_pfsa'),
    path('contact/', views.contact_us, name='contact_us'),
]
