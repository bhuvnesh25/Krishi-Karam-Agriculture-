from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate,get_user_model,login,logout

from .models import *




def home(request):
    return render(request, 'index.html', {"title":"Home"})

def about(request):
    return render(request, 'about.html', {"title": "about"})

def contact(request):
    return render(request, 'contact.html',{"title":"contact"})

def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User.objects.filter(mobile=username).first()
        if user:
            if user.aadhaar==password:
                return HttpResponse("successfully Login")
            else:
                return HttpResponse("Invalid password")
        else:
            return HttpResponse("Invalid Mobile no")
    return render(request, 'form.html', {})


def signup_view(request):
    return render(request, 'form.html', {})


def logout_view(request):
    return render(request, 'form.html', {})