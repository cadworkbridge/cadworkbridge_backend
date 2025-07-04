from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework.views import APIView


# Create your views here.
def auth(request):
    return render(request, "authentication/auth_ui.html")



def reset(request):
    return render(request, "authentication/reset_password.html")


def profile(request):
    return render(request, "authentication/profile.html")

def reset_password_confirm(request, uid, token):
    return render(request, "authentication/reset_password_confirm.html", {"uid": uid, "token": token})

def set_password(request):
    return render(request, "authentication/set_password.html")




