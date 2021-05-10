from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
#from .models import Contact, Blog, Course
# Create your views here.
#from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


#string-->http response
def index(request):
    return render(request,['wingsApp/index.html'])

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created for '+form.cleaned_data.get('username'))
            return redirect('loginPage')

    context={'form':form}
    return render(request,'wingsApp/register.html',context)




def loginPage(request):
    if request.method=='POST':
        #taking thr value of these fields
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        user =authenticate(request,first_name=fname,last_name=lname)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'email or password is incorrect')

    context={}
    return render(request,['wingsApp/login.html'],context)