from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RecruiterHomeView(LoginRequiredMixin, TemplateView):
    template_name = "recruiters/home.html"


class JobsPostedView(LoginRequiredMixin, TemplateView):
    template_name = "recruiters/jobs_posted.html"

