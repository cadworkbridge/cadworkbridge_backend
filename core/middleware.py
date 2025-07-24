# core/middleware.py
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get('access')
        if token:
            try:
                validated_token = JWTAuthentication().get_validated_token(token)
                request.user = JWTAuthentication().get_user(validated_token)
            except:
                pass
