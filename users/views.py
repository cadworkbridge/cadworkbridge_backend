from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView
from rest_framework.views import APIView
from django.conf import settings
from djoser.social.views import ProviderAuthView
from .utils import set_jwt_cookies

# ✅ Converts a Django session into JWT cookies (for use after social login)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def session_to_jwt(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    logout(request)  # Logs out the session-based login
    response = Response({"detail": "JWT issued from session"})
    return set_jwt_cookies(response, str(refresh.access_token), str(refresh))

# ✅ Handles Google login with Djoser social and sets cookies if login successful
class CustomProviderAuthView(ProviderAuthView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")
            return set_jwt_cookies(response, access_token, refresh_token)

        return response

# ✅ Custom login view to return 200 with JWT cookies instead of raw tokens
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

# ✅ Refreshes JWT using the cookie-stored refresh token
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"])
        if refresh_token:
            request.data["refresh"] = refresh_token  # Inject token into request data

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")
            return set_jwt_cookies(response, access_token, refresh_token)

        return response

# ✅ Verifies JWT using the access token from cookies
class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE"])
        if access_token:
            request.data["token"] = access_token  # Inject token into request data
        return super().post(request, *args, **kwargs)

# ✅ Logs out by removing access and refresh tokens from browser cookies
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response({"detail": "Logged out."}, status=204)
        response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE"])
        response.delete_cookie(settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"])
        return response
