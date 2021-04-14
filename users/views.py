from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm


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

