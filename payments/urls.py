# app/urls.py
from django.urls import path
from .views import VerifyActivationView

app_name = 'payments'

urlpatterns = [
    path("verify-activation/", VerifyActivationView.as_view()),
]
