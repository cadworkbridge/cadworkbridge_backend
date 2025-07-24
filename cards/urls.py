from django.urls import path
from .views import CardListView, CardDetailView

app_name = 'cards'
urlpatterns = [
    path('', CardListView.as_view(), name='card-list'),               # e.g. /cards/
    path('<int:pk>/', CardDetailView.as_view(), name='card-detail'),  # e.g. /cards/1/
]