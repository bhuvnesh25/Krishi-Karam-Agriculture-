from django.shortcuts import render, HttpResponse, redirect
import sendgrid
from sendgrid.helpers.mail import *
from .models import *




def home(request):
    return render(request, 'index.html', {"title":"Home"})

def about(request):
    return render(request, 'about.html', {"title": "about"})

def services(request):
    return render(request, 'serve.html',{"title":"services"})

def detail(request):
    return render(request, '',{"title":"detail"})

def buy(request):
    return render(request, 'buy_sell.html',{"title":"buy"})


def news(request):
    return render(request, 'news.html',{"title":"news"})


def contact(request):
    return render(request, 'contact.html',{"title":"contact"})

def event(request):
    return render(request, 'event.html',{"title":"event"})

def buy_sell(request):

    if request.session.has_key("user"):

        return render(request, 'buy.html', {"title": "buy_sell",
                                            "status": True})
    else:
        return redirect("login")



def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User.objects.filter(mobile=username).first()
        if user:
            if user.aadhaar==password:
                request.session['user'] = username
                return redirect("buy_sell")

            else:
                return render(request, 'index.html', {"error": "invalid password"})
        else:
            return render(request, 'index.html', {"error": "Invalid mobile"})
    return render(request, 'index.html', {"error": "Invalid mobile"})



def signup_view(request):
    if request.method == "POST":
        name =request.POST.get("name")
        state = request.POST.get("state")
        mobile = request.POST.get("mobile")
        city= request.POST.get("city")
        aadhaar = request.POST.get("aadhaar")
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
            user = User(email=email, address_id=address_id, name=name, aadhaar=aadhaar, mobile=mobile)
            user.save()
            try:
                sg = sendgrid.SendGridAPIClient(apikey="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")
                from_email = Email("info@krishikaram.com")
                to_email = Email(email)
                subject = "Welcome to krishikaram"
                content = Content("text/plain", "you are successfully registered to Krishikaram")
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                print(response)
            except Exception as e:

                print(e)
            return render(request, 'index.html', {"error": "Register successful"})
        except Exception as e:
            print(e)
    return render(request, 'index.html', {"error": "Worked"})


def logout_view(request):
    del request.session["user"]
    return redirect("home")