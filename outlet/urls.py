from django.urls import path, include
from django.contrib import admin
from .views import *
app_name = 'outlet'

urlpatterns = [

    path('regis-outlet', regis, name='regis'),
    path('update-outlet/<slug>', update_outlet, name='update'),




]
