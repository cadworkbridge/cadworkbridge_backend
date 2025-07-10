from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import CardModel
from .serializers import CardListSerializer, CardDetailSerializer

class CardListView(ListAPIView):
    """GET /cards/ — list all cards"""
    queryset = CardModel.objects.all()
    serializer_class = CardListSerializer


class CardDetailView(RetrieveAPIView):
    """GET /cards/<id>/ — get a single card"""
    queryset = CardModel.objects.all()
    serializer_class = CardDetailSerializer
