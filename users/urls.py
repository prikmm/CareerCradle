from django.urls import path
from .views import UsertypeRedirectView, FillUsertypeView

app_name = 'users'

urlpatterns = [
    path('redirect', UsertypeRedirectView.as_view(), name='redirect'),
    path('usertype', FillUsertypeView.as_view(), name='usertype')
]