from django.urls import path
from .views import CardListView, CardListItemView

app_name = 'api'  # The app name for namespace purposes

urlpatterns = [
    path('cards/', CardListView.as_view(), name='card_list'),  # List view of all cards with trailing slash
    path('card-item/<int:pk>/', CardListItemView.as_view(), name='card_item'),  # Detail view of a specific card
]
