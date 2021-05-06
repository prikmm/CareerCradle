from django.urls import path
from .views import CandidateHomeView, JobsAppliedView
from .views import JobsView


app_name = 'candidates'

urlpatterns = [
    path('home/', CandidateHomeView.as_view(), name='home'),
    path('home/avail_jobs/',JobsView.as_view(), name = "avail_jobs"),
    path('Dashboard/', JobsAppliedView.as_view(), name="dashboard")
]
