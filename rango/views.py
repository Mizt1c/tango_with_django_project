from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    HttpResponse("<a href='/rango/about/'>About</a>")
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says here is the about page.")
