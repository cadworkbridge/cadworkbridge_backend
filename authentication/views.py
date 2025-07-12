from django.shortcuts import render,redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from .utils import set_jwt_cookies

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
    logout(request)

    response = Response({"detail": "JWT issued from session"})
    return set_jwt_cookies(response, str(refresh.access_token), str(refresh))


class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            data = response.data
            access_token = data.get("access")
            refresh_token = data.get("refresh")

            res = Response({"detail": "Login successful"}, status=200)
            return set_jwt_cookies(res, access_token, refresh_token)
        return response