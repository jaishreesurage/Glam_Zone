from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .models import Profile

# Create your views here.

# logo view 
def LogoPage(request):
    return render(request,"app/logo.html")

#welcome view 
def welcome(request):
    return render(request, "app/welcome.html")

# =========================
# SIGNUP VIEW
# =========================
def signup_page(request):

    # check form submit
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")


        # check username already exist
        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists")
            return redirect("signup_page")


        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        # create profile
        Profile.objects.create(
            user=user,
            full_name=full_name,
            email=email,
            
        )


        messages.success(request, "Signup successful")
        return redirect("login_page")


    return render(request, "app/signup.html")



# =========================
# LOGIN VIEW
# =========================
def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        # authenticate user
        user = authenticate(request, username=username, password=password)


        if user is not None:

            login(request, user)

            return redirect("login_success")

        else:

            messages.error(request, "Invalid username or password")
            return redirect("login_page")


    return render(request, "app/login.html")



# =========================
# LOGIN SUCCESS VIEW
# =========================
def login_success(request):

    return render(request, "app/login_success.html")


def brands(request):

    return render(request, 'app/brands.html')


