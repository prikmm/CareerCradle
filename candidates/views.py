from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CandidateHomeView(LoginRequiredMixin, TemplateView):
    template_name = "candidates/home.html"

class JobsView(TemplateView):
    template_name = "candidates/avail_jobs.html"

class JobsAppliedView(TemplateView):
    template_name = "candidates/jobs_applied.html"