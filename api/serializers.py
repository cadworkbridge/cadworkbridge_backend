from rest_framework import serializers
from .models import CardModel

class CardListSerializer(serializers.ModelSerializer):
    """Serializer for listing cards (brief info)."""
    image = serializers.URLField(source='image.url', read_only=True)


    class Meta:
        model = CardModel
        fields = ['id', 'title', 'image']
        read_only_fields = ['id']


class CardDetailSerializer(serializers.ModelSerializer):
    """Serializer for a single card (full detail)."""
    image = serializers.URLField(source='image.url', read_only=True)
    pdf_file = serializers.URLField(source='pdf_file.url', read_only=True)
    extra_file = serializers.URLField(source='extra_file.url', read_only=True)

    class Meta:
        model = CardModel
        fields = ['id', 'title', 'description', 'image', 'youtube_link', 'pdf_file', 'extra_file','video_length', 'language', 'price']
        read_only_fields = ['id']
