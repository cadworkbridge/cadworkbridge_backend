from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from datetime import timedelta

from .serializers import ActivationRequestSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

class VerifyActivationView(APIView):
    def post(self, request):
        serializer = ActivationRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
                if user.is_active and user.is_app_active:
                    token = AccessToken()
                    token.set_exp(lifetime=timedelta(days=365))
                    token["email"] = email
                    token["type"] = "activation"
                    return Response({"status": "active", "token": str(token)})
            except User.DoesNotExist:
                pass
            return Response({"status": "inactive"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
