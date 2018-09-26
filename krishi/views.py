from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate,get_user_model,login,logout

from .forms import UserLoginForm




def home(request):
    return render(request, 'index.html', {"title":"Home"})

def about(request):
    return render(request, 'about.html', {"title": "about"})

def contact(request):
    return render(request, 'contact.html',{"title":"contact"})

def login_view(request):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

    return render(request, 'form.html', {"form":form})


def signup_view(request):
    return render(request, 'form.html', {})


def logout_view(request):
    return render(request, 'form.html', {})