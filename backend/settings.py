from pathlib import Path
import environ
from datetime import timedelta
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Set up environment variables
env = environ.Env()
env.read_env(BASE_DIR / ".env")

# ------------------------------
# General Settings
# ------------------------------
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = [
    "http://localhost:3000",  # Frontend URL
    "https://www.cadworkbridge.com",  # Production domain
    "https://backend-default.fly.dev",  # Deployed backend
    "localhost",  # Localhost for development
    "127.0.0.1",  # Local IP for development
    "127.0.0.1:8000",  # Localhost with port
    "localhost:8000",  # Localhost with port
]

# ------------------------------
# Installed Apps
# ------------------------------
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for allauth

    # Third-party apps
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    #'social_django',
    'cloudinary',
    'cloudinary_storage',


    # Internal apps
    'authentication',
    'api',
    'core',
    'accounts',
]

# ------------------------------
# Middleware
# ------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------
# CORS & CSRF Settings
# ------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend URL
    "https://www.cadworkbridge.com",  # Production domain
    "https://backend-default.fly.dev",  # Deployed backend
]

CSRF_TRUSTED_ORIGINS = [
    "https://backend-default.fly.dev",
    "https://www.cadworkbridge.com",
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True

# ------------------------------
# URL Configuration
# ------------------------------
ROOT_URLCONF = 'backend.urls'

# ------------------------------
# Template Settings
# ------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------------------------
# WSGI Application
# ------------------------------
WSGI_APPLICATION = 'backend.wsgi.application'

# ------------------------------
# Database Configuration
# ------------------------------
DATABASES = {
    'default': env.db("DATABASE_URL")
}

# ------------------------------
# Password Validation
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    # Uncomment to enable password validators
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ------------------------------
# Localization
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# Static Files
# ------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Required for deployment (e.g. Render)
STATICFILES_DIRS = [BASE_DIR / 'static']  # Global static folder (for custom CSS/JS)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ------------------------------
# Default Auto Field
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------
# Django Rest Framework
# ------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# ------------------------------
# Custom User Model
# ------------------------------
AUTH_USER_MODEL = 'accounts.User'

# ------------------------------
# Simple JWT Settings
# ------------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# ------------------------------
# Djoser Settings
# ------------------------------
DJOSER = {
    "LOGIN_FIELD": "email",  # Use email (not username) to log in
    "USER_CREATE_PASSWORD_RETYPE": False,  # Don't require password re-entry on registration
    "SEND_ACTIVATION_EMAIL": False,  # Skip sending activation email after registration
    "SERIALIZERS": {
        "user_create": "accounts.serializers.CustomUserCreateSerializer",  # Controls registration input
        "user": "accounts.serializers.CustomUserSerializer",  # Controls how other users are serialized
        "current_user": "accounts.serializers.CustomUserSerializer",  # Controls /auth/users/me/ response
    },
    "PASSWORD_RESET_CONFIRM_URL": "authentication/reset_password_confirm/{uid}/{token}/",
    "TOKEN_MODEL": None,  # Disable Djoser token model (using JWT instead)
}

# ------------------------------
# Site Settings
# ------------------------------
SITE_ID = 2  # Set the correct site ID in the database

# ------------------------------
# Email Settings
# ------------------------------
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env.int("EMAIL_PORT")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# ------------------------------
# Cloudinary Storage
# ------------------------------
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': env("CLOUDINARY_API_KEY"),
    'API_SECRET': env("CLOUDINARY_API_SECRET"),
}

cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
    secure=True
)
