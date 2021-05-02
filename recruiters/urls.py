from django.urls import path
from .views import RecruiterHomeView


app_name = 'recruiters'

urlpatterns = [
    path('home/', RecruiterHomeView.as_view(), name='home'),
]