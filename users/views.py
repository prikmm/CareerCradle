from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm
from django.views.generic.base import RedirectView
from .models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

# Create your views here.
class AuthView(TemplateView):

    def get(self, request):
        context = {
            'login_form': LoginForm(),
            'signup_form': UserCreationForm(request.POST or None),
        }
        return render(request, 'auth.html', context)

    def post(self, request):
        
        return render(request, 'select.html')

class SelectView(TemplateView):

    def get(self, request):
        return render(request, 'select.html')


class UsertypeRedirectView(LoginRequiredMixin, View):

    def get(self, request):
        current_user = request.user
        print(current_user.usertype)
        if current_user.usertype == 1: # Candidate
            return HttpResponseRedirect(reverse("candidates:home"))
        elif current_user.usertype == 0: # Recruiter
            return HttpResponseRedirect(reverse("recruiters:home"))
        
        return HttpResponseForbidden()


