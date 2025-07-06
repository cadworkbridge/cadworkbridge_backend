from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CardModel  # Import the model
from .serializers import CardListSerializer,CardListItemSerializer # Import the list serializer

class CardListView(APIView):
    def get(self, request):
        # Fetch all cards from the database
        cards = CardModel.objects.all()

        # Serialize the data using CardListSerializer
        serializer = CardListSerializer(cards, many=True)

        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)

class CardListItemView(APIView):
    def get(self, request, pk):
        # Fetch a single card by its primary key (ID)
        try:
            card = CardModel.objects.get(pk=pk)
        except CardModel.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the card data using CardListItemSerializer
        serializer = CardListItemSerializer(card)

        # Return the serialized card data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)