from django.shortcuts import render
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,['wings/index.html'])

def signIn(request):


    return render(request,['wings/signIn.html'])


def logIn(request):
    return render(request,['wings/logIn.html'])