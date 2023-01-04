from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import student

# Create your views here.
def home(request):
    students = student.objects.all()
    return render(request,'studentmain.html',{'students':students})
    
def about(request):
    return render(request,"studentabout.html")

def studentcreate(request):
    if request.method == "POST":
        if request.POST.get("name") \
            and request.POST.get("email")\
            and request.POST.get("city")\
            and request.POST.get("phone"):
            students = student()
            students.name = request.POST.get("name")
            students.email = request.POST.get("email")
            students.city = request.POST.get("city")
            students.phone = request.POST.get("phone")
            students.save()
            return HttpResponseRedirect("/home")
    else:
        return render(request,"home.html")

def editstudent(request):
    if request.method == "POST":
        students = student.objects.get(id = request.POST.get("id"))
        if students != None:
            students.name = request.POST.get("name")
            students.email = request.POST.get("email")
            students.city = request.POST.get("city")
            students.phone = request.POST.get("phone")
            students.save()
            return HttpResponseRedirect("/home")


def deletestudent(request, student_id):
    students = student.objects.get(id = student_id)
    students.istrue = 'False'
    students.save()
    return HttpResponseRedirect("/home")


def logout(request):
    auth.logout(request)
    return redirect("/home")