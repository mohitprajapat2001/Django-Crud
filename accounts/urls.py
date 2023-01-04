from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('register', views.register, name="Register"),

]
