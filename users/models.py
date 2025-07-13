from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email).lower()  # Normalize and lowercase
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save to the correct DB
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Ensure superuser flags
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields['is_staff']:
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields['is_superuser']:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)                      # Unique identifier
    is_active = models.BooleanField(default=True)               # Active status
    is_staff = models.BooleanField(default=False)               # Admin access
    date_joined = models.DateTimeField(default=timezone.now)    # Join date
    last_login = models.DateTimeField(default=timezone.now)     # Last login

    USERNAME_FIELD = 'email'    # Use email to log in
    REQUIRED_FIELDS = []        # No extra required fields

    objects = UserManager()     # Custom manager

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

# Optional profile model
class Profile(models.Model):
    """
    Extended user information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email}'s profile"
