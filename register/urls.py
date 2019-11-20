from django.contrib import admin
from django.urls import path
from . import views

# app_name = 'register'

urlpatterns = [
    path('profile/', views.dynamic_lookup_view , name='reg-g-profile'),
    path('<str:username>', views.dynamic_lookup_view, name='reg-profile')
    ]