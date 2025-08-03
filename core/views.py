from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import CardModel
from .serializers import CardListSerializer, CardDetailSerializer
from django.shortcuts import render

def homepage(request):
    cards = CardModel.objects.all()
    return render(request, 'core/home.html', {'cards': cards})




class CardListView(ListAPIView):
    """GET /cards/ — list all cards"""
    queryset = CardModel.objects.all()
    serializer_class = CardListSerializer




class CardDetailView(RetrieveAPIView):
    """GET /cards/<id>/ — get a single card"""
    queryset = CardModel.objects.all()
    serializer_class = CardDetailSerializer

