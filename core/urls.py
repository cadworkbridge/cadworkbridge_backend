from django.urls import path
from . import views

app_name = 'core'  # The app name for namespace purposes

urlpatterns = [
    path('', views.core, name='core'),  # List view of all cards


]
