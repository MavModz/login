from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout as authlogout

# Create your views here.
def home(request):
    return render(request, "secure/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name

        myuser.save()
        messages.success(request, "Account Created Successfully")
        return redirect("login")


    return render(request, "secure/signup.html")

def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            authlogin(request, user)
            name = user.first_name
            return render(request, "secure/index.html", {"name": name})
        
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")

    return render(request, "secure/login.html")

def logout(request):
    authlogout(request)
    return redirect("home")