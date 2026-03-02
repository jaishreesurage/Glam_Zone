from django.shortcuts import render
from.models import *

# Create your views here.

# logo view 
def LogoPage(request):
    return render(request,"app/logo.html")

#welcome view 
def welcome(request):
    return render(request, "app/welcome.html")

