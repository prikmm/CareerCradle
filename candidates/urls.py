from django.urls import path
from .views import CandidateHomeView


app_name = 'candidates'

urlpatterns = [
    path('home/', CandidateHomeView.as_view(), name='home'),
]