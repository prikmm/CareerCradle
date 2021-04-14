from django.contrib import admin
from django.urls import path
from django.urls.conf import include

app_name = 'users'

urlpatterns = [
    path('', include('allauth.urls')),
]