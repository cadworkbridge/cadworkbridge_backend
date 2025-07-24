from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    path("session-to-jwt/", views.session_to_jwt, name="session-to-jwt"),
    path("jwt/provider/", views.CustomProviderAuthView.as_view(), name="cookie_token_provider"),
    path("jwt/create/", views.CookieTokenObtainPairView.as_view(), name="cookie_token_obtain_pair"),
    path("jwt/refresh/", views.CustomTokenRefreshView.as_view(), name="cookie_token_refresh"),
    path("jwt/verify/", views.CustomTokenVerifyView.as_view(), name="cookie_token_verify"),
    path("logout/", views.LogoutView.as_view(), name="cookie_token_logout"),
    path("verify-activation/", views.VerifyActivationView.as_view()),

    # ✅ Google redirect page after login

]
