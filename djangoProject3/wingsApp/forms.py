from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

#create a form that will inheritae UserCreationForm to customize it
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        #these are the fields that we want
        fields=['first_name','last_name','username','email','password1','password2']
