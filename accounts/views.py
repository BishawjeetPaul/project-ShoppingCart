from django.shortcuts import render
from django.http import HttpResponse


# This function for new user registration.
def register(request):
    return render(request, "accounts/register.html")


# This function for user login.
def login(request):
    return render(request, "accounts/login.html")


# This function for user logout.
def logout(request):
    return HttpResponse("logout page")