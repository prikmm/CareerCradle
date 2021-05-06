from django.urls import path
from .views import RecruiterHomeView, JobsPostedView


app_name = 'recruiters'

urlpatterns = [
    path('home/', RecruiterHomeView.as_view(), name='home'),
    path('home/dashboard/', JobsPostedView.as_view(), name='jobs_posted'),
]