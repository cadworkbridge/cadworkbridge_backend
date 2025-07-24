# payments/serializers.py

from rest_framework import serializers

class ActivationRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
