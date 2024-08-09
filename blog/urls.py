from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('login',views.login_page, name='login'),
]
