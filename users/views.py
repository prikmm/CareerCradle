from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from .models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .forms import UserTypeForm

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
        if current_user.usertype == 1: # Candidate
            return HttpResponseRedirect(reverse("candidates:home"))
        elif current_user.usertype == 0: # Recruiter
            return HttpResponseRedirect(reverse("recruiters:home"))
        elif not current_user.is_staff:
            return HttpResponseRedirect(reverse("users:usertype"))
            
        return HttpResponseForbidden()

class FillUsertypeView(LoginRequiredMixin, View):
    
    def get(self, request):
        current_user = request.user
        if current_user.usertype:
            return HttpResponseRedirect(reverse("users:redirect"))
        else:
            context = {
                'usertype_form': UserTypeForm(),
            }
            return render(request, "users/usertype.html", context)

    def post(self, request):
        user_type_form = UserTypeForm(request.POST)
        if user_type_form.is_valid():
            user_type_form.save(request)
        return HttpResponseRedirect(reverse("users:redirect"))

        
class ContactUsView(TemplateView):
    template_name = "users/contact.html"

class AboutUsView(TemplateView):
    template_name = "users/about.html"

