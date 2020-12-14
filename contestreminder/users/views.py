from django.shortcuts import render
import requests

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(UpdateView):
    model = CustomUser
    # form_class = CustomUserChangeForm
    fields=['codeChef', 'codeForces', 'hackerEarth', 'hackerRank', 'spoj']
    success_url = reverse_lazy('profile')
    template_name = 'user/profile.html'

    def get_object(self):
        return self.request.user

class DeleteUserView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'user/delete.html'

    def get_object(self):
        return self.request.user

def contribute(request):
    contributors = {}
    url = 'https://api.github.com/repos/codestromer/ContestReminder/contributors'
    response = requests.get(url)
    contributors = response.json()
    return render(request, 'about.html', {'contributors': contributors})
