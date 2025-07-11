from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def session_to_jwt(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })


def google_redirect(request):
    return render(request, "authentication/google_redirect.html")


