from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
path('register',views.register,name='register'),
path('loginPage',views.loginPage,name='loginPage'),

    ]