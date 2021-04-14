from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
]