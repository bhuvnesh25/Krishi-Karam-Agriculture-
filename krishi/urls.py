"""krishi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="index"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("event",event, name="event"),
    path("services",services, name="services"),
    path("news",news, name="news"),
    path("buy",buy, name="buy"),
    path("detail",detail, name="detail"),
    path("info",info, name="info"),
    path("search",search, name="search"),
    path("login", login_view ,name="login"),
    path("signup", signup_view,name="signup"),
    path("logout", signup_view,name="logout"),
    path("payment",payment,name="payment"),
]