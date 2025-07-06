# serializers.py
from rest_framework import serializers
from .models import CardModel

class CardListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = ['id', 'title', 'description', 'image', 'youtube_link', 'pdf_file', 'extra_file']

class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = ['id', 'title', 'description', 'image']
