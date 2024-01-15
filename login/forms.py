from .models import *
from django import forms  
from django.contrib.auth.forms import UserCreationForm

class signUpForm(UserCreationForm):
     class Meta:
        model = Userprofile
        fields = ['name', 'username', 'email', 'phone_number', 'place', 'password1','password2']
class loginForm(UserCreationForm):
     class Meta:
        model = Userprofile
        fields = ['username','password1']