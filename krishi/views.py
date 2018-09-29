from django.shortcuts import render, HttpResponse, redirect
import sendgrid
from sendgrid.helpers.mail import *
from .models import *

from django.core.cache import cache
cache.clear()


def home(request):
    return render(request, 'index2.html', {"title":"Home"})


def about(request):
    return render(request, 'about.html', {"title": "about"})


def services(request):
    return render(request, 'serve.html',{"title":"services"})


def detail(request):
    return render(request, 'regis.html',{"title":"detail"})


def info(request):
    return render(request, 'info.html',{"title":"info"})


def news(request):
    return render(request, 'news.html',{"title":"news"})


def payment(request):
    return render(request, 'payment.html',{"title":"payment"})


def contact(request):
    return render(request, 'contact.html',{"title":"contact"})


def event(request):
    return render(request, 'event.html',{"title":"event"})


def search(request):
    if request.session.has_key("user"):
        if request.method == "POST":
            query = request.POST.get("query")

            crop = Data.objects.filter(crop_name=query).first()

            if crop:
                print(crop)
                return render(request, 'search.html', {"title": "search",
                                                       "status": True,
                                                       "data": crop})
            else:
                return render(request, 'search.html', {"title": "search",
                                                       "status": True,
                                                       "data": False})

        else:
            return render(request, 'search.html', {"title": "search",
                                                   "status": True})
    else:
        return redirect("login")


def buy(request):

    if request.session.has_key("user"):

        return render(request, 'buy_sell.html', {"title": "buy",
                                                 "status": True})
    else:
        return redirect("login")


def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User.objects.filter(mobile=username).first()
        if user:
            if user.password==password:
                request.session['user'] = username
                return redirect("search")

            else:
                return render(request, 'index2.html', {"error": "invalid password"})
        else:
            return render(request, 'index2.html', {"error": "Invalid mobile"})
    return render(request, 'index2.html', {"error": "Invalid mobile"})


def signup_view(request):
    if request.method == "POST":
        name =request.POST.get("name")
        state = request.POST.get("state")
        mobile = request.POST.get("mobile")
        city= request.POST.get("city")
        password = request.POST.get("aadhaar")
        locality = request.POST.get("locality")
        pin = request.POST.get("pin")
        sub_locality = request.POST.get("sub_locality")
        email = request.POST.get("email")


        try:
            address = Address(state=state, city=city, locality=locality, sub_locality=sub_locality, pin=pin)
            address.save()
            address_id = address.id
        except Exception as e:
            print(e)

        try:
            user = User(email=email, address_id=address_id, name=name, password=password, mobile=mobile)
            user.save()
            try:
                sg = sendgrid.SendGridAPIClient(apikey="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")
                from_email = Email("info@krishikaram.com")
                to_email = Email(email)
                subject = "Welcome to krishikaram"
                content = Content("text/plain", "you are successfully registered to Krishikaram")
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                print(str(response))
            except Exception as e:
                print(e)
            return render(request, 'index2.html', {"error": "Register successful"})
        except Exception as e:
            return render(request, 'index2.html', {"error": e})
    return render(request, 'index2.html', {"error": False})


def logout_view(request):
    del request.session["user"]
    return redirect("home")