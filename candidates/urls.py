from django.urls import path
from .views import CandidateHomeView
from .views import JobsView
from .views import ContactView
from .views import AboutView


app_name = 'candidates'

urlpatterns = [
    path('home/', CandidateHomeView.as_view(), name='home'),
    path('home/avail_jobs/',JobsView.as_view(), name = "avail_jobs"),
    path('home/contact/', ContactView.as_view(), name='contact'),
    path('home/about/', AboutView.as_view(), name='about'),
]