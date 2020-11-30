from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email','codeChef', 'codeForces', 'hackerEarth', 'hackerRank', 'spoj')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('codeChef', 'codeForces', 'hackerEarth', 'hackerRank', 'spoj')
