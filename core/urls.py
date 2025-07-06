from django.urls import path
from . import views

app_name = 'core'  # The app name for namespace purposes

urlpatterns = [
    path('', views.core, name='core'),  # List view of all cards
    path('contact', views.core, name='contact'),  # List view of all cards

]
