from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("home of Home")

def contact(request):
    return HttpResponse("contact of Home")

def about(request):
    return HttpResponse("about of Home")