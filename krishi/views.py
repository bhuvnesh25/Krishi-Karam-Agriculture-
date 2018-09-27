from django.shortcuts import render, HttpResponse


from .models import *




def home(request):
    return render(request, 'index.html', {"title":"Home"})

def about(request):
    return render(request, 'about.html', {"title": "about"})

def contact(request):
    return render(request, 'contact.html',{"title":"contact"})

def event(request):
    return render(request, 'event.html',{"title":"event"})

def buy_sell(request):
    return render(request, 'buy.html',{"title":"buy_sell"})

def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User.objects.filter(mobile=username).first()
        if user:
            if user.aadhaar==password:
                return HttpResponse("success login")
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


        try:
            address = Address(state=state, city=city, locality=locality, sub_locality=sub_locality, pin=pin)
            address.save()
            address_id = address.id
        except:
            return HttpResponse("Something went wrong with database")

        try:
            user = User(address_id=address_id,name=name, aadhaar=aadhaar, mobile=mobile)
            user.save()
            return render(request, 'index.html', {"error": "Register successful"})
        except:
            return HttpResponse("Something went wrong with database")
    return render(request, 'index.html', {"error": "Worked"})


def logout_view(request):
    return render(request, 'form.html', {})