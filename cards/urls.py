from django.urls import path
from .views import CardListView, CardDetailView

app_name = 'api'
urlpatterns = [
    path('cards/', CardListView.as_view(), name='card-list'),               # e.g. /cards/
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card-detail'),  # e.g. /cards/1/
]