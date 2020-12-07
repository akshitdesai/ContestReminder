from django.shortcuts import render
import requests

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def contribute(request):
    contributors = {}
    url = 'https://api.github.com/repos/codestromer/ContestReminder/contributors'
    response = requests.get(url)
    contributors = response.json()
    return render(request, 'about.html', {'contributors': contributors})
