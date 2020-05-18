from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('index',views.index,name='index'),
    path('update',views.update,name='update'),
    path('logout',views.logout,name='logout'),
    path('otpverify',views.otpverify,name='otpverify'),
    path('delete',views.delete,name='delete'),
    path('loginToregister',views.loginToregister,name='loginToregister'),
    path('register',views.register,name='register'),
]