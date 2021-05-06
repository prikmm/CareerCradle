from django.urls import path
from .views import UsertypeRedirectView, FillUsertypeView, AboutUsView, ContactUsView

app_name = 'users'

urlpatterns = [
    path('redirect', UsertypeRedirectView.as_view(), name='redirect'),
    path('usertype', FillUsertypeView.as_view(), name='usertype'),
    path('about/', AboutUsView.as_view(), name='aboutus'),
    path('contact/', ContactUsView.as_view(), name='contactus'),
]