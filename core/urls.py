from django.urls import path
from .views import CardListView, CardDetailView,homepage

app_name = 'core'
urlpatterns = [
    path('cards/', CardListView.as_view(), name='card-list'),               # e.g. /cards/
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card-detail'),  # e.g. /cards/1/
    path('', homepage, name='core'),  # List view of all cards

]