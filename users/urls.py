from django.urls import path
from .views import UsertypeRedirectView

app_name = 'users'

urlpatterns = [
    path('redirect', UsertypeRedirectView.as_view(), name='redirect')
]