from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.core, name='homepage' ),  # This will serve /
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('log_out/', views.log_out, name='log_out'),
    path('contact/', views.contact, name='contact'),

]