from djoser.serializers import UserCreatePasswordRetypeSerializer
from rest_framework import serializers
from .models import CustomUser


class UserCreateSerializer(UserCreatePasswordRetypeSerializer):
    """
    Serializer for creating a new CustomUser instance.
    Inherits from Djoser's UserCreatePasswordRetypeSerializer to handle
    email, password, and re_password fields for user registration.
    """
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = CustomUser
        fields = (
            'id',
            'email',
            'password',
            're_password',  # Required due to USER_CREATE_PASSWORD_RETYPE=True in settings
        )
        # You can add extra_kwargs for fields if needed, e.g., to make password write-only
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for representing CustomUser instances for read-only operations
    or for updates (excluding password).
    This is often used for the 'me/' endpoint or user profile views.
    """
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'is_active',
            'is_staff',
            'is_app_active',
            # Add any other fields you want to expose or allow for update
            # e.g., 'date_joined' if you add it to your model
        )
        read_only_fields = (
            'email',  # Email is typically not changeable after creation, or handled separately by Djoser's email reset
            'is_active',
            'is_staff',
            'is_app_active', # <-- Add this line
        )
class ActivationRequestSerializer(serializers.Serializer):
    """
    Serializer for the VerifyActivationView, expecting an email.
    """
    email = serializers.EmailField(required=True)
