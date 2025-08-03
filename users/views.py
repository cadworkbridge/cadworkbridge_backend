# users/views.py
from datetime import timedelta
from django.contrib.auth import get_user_model # Recommended way to get the custom user model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import ActivationRequestSerializer # Import your new serializer
from django.views import View
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from django.conf import settings

# Get the CustomUser model
User = get_user_model()

class VerifyActivationView(APIView):
    """
    Check if user is active and issue long-lived token.
    This view expects an email in the request body.
    If the user exists, is_active, and is_app_active, it issues a JWT Access Token.
    """

    def post(self, request):
        """
        Return activation token if user is active and app-active.
        """
        serializer = ActivationRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
                # Check both Django's is_active and your custom is_app_active
                if user.is_active and user.is_app_active:
                    # Create a JWT Access Token
                    token = AccessToken.for_user(user)
                    # Set a long lifetime as requested (365 days)
                    # Be cautious with very long-lived tokens in production; consider refresh tokens.
                    token.set_exp(lifetime=timedelta(days=365))

                    # You can add custom claims to the token if needed
                    # token["custom_data"] = "some_value"

                    return Response({
                        "status": "active",
                        "token": str(token)
                    }, status=status.HTTP_200_OK)
                else:
                    # User exists but is not active or not app-active
                    return Response({
                        "status": "inactive",
                        "message": "User account is not active or app access is restricted."
                    }, status=status.HTTP_200_OK) # Return 200 OK as it's a valid check result
            except User.DoesNotExist:
                # User does not exist, return inactive status to avoid leaking user existence
                return Response({
                    "status": "inactive",
                    "message": "User not found or account is not active."
                }, status=status.HTTP_200_OK) # Return 200 OK as it's a valid check result
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SocialAuthCompleteView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')

        login(request, user)

        refresh = RefreshToken.for_user(user)
        response = redirect('/')

        response.set_cookie(
            key='access_token',
            value=str(refresh.access_token),
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Lax',
            max_age=getattr(settings, 'ACCESS_TOKEN_LIFETIME_SECONDS', 300)
        )
        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Lax',
            max_age=getattr(settings, 'REFRESH_TOKEN_LIFETIME_SECONDS', 86400)
        )

        return response
