from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('auth_ui/', views.auth, name='auth_ui'),
    path('reset_password/', views.reset, name='reset_password'),
    path('profile/', views.profile, name='profile'),
    path("reset_password_confirm/<uid>/<token>/", views.reset_password_confirm, name="reset-password-confirm"),
    path('set-password/', views.set_password, name='set_password'),
    path("session-to-jwt/", views.session_to_jwt, name="session-to-jwt"),
    # ✅ Google redirect page after login
    path("google-redirect/", views.google_redirect, name="google-redirect"),

]
