from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout


def core(request):
    return render(request, 'core/core.html')

def register(request):
    return render(request, "core/register.html")

def login(request):
    return render(request, "core/login.html")

def log_out(request):
    logout(request)  # clears session
    return redirect('homepage')  # or 'login'

def contact(request):
    return render(request, "core/contact.html")