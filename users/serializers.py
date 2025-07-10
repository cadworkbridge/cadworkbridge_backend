from djoser.serializers import UserCreateSerializer, UserSerializer, ValidationError
from users.models import User

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "password")  # 👈 no re_password

    def validate_password(self, value):
        """Custom password validation (optional). For example, enforce minimum length."""
        if len(value) < 4:
            raise ValidationError("Password must be at least 4 characters long.")
        return value

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ("id", "email")
