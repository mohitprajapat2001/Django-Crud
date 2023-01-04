from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="student home"),
    path('about', views.about, name="student about"),
    path('studentcreate', views.studentcreate, name="studentcreate"),
    path('editstudent', views.editstudent, name="editstudent"),
    path('deletestudent/<str:student_id>', views.deletestudent, name="deletestudent"),
    path('logout', views.logout, name="student logout"),

]
