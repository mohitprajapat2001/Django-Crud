from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, "index.html")

def navigation(request):
    return render(request, "webnavigator.html")