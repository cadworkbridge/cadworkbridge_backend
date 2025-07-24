from djoser.serializers import UserCreateSerializer, UserSerializer, ValidationError
from users.models import User
from rest_framework import serializers


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "first_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        if len(value) < 4:
            raise ValidationError("Password must be at least 4 characters long.")
        return value


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ("id", "email")



class ActivationRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()