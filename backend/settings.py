from pathlib import Path
import environ
from datetime import timedelta
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")  # Django's cryptographic key (keep secret in production)
DEBUG = env.bool("DEBUG", default=True)  # Enable debug mode (set to False in production)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])  # Domains that can serve the app


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'storages',
    'cloudinary',
    'cloudinary_storage',
    'cards',
    'cadwork',
    'payments',
    'core',
    'users',
    'django_filters',
    'drf_spectacular',
    # Allauth core
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Add your social provider (e.g. Google)
    'allauth.socialaccount.providers.google',
]



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',                    # Handles CORS
    'django.middleware.security.SecurityMiddleware',            # Basic security headers
    'whitenoise.middleware.WhiteNoiseMiddleware',               # Serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',     # Enable sessions
    'django.middleware.common.CommonMiddleware',                # Common utilities
    'django.middleware.csrf.CsrfViewMiddleware',                # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests
    'allauth.account.middleware.AccountMiddleware',             # Allauth session handling
    'django.contrib.messages.middleware.MessageMiddleware',     # Flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Prevent clickjacking
    'core.middleware.JWTAuthMiddleware' #Django middleware, you can access user info (request.user) anywhere in your backend
]





CORS_ALLOW_CREDENTIALS = True  # Allow cookies/headers in cross-origin requests
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])  # Frontend domains allowed to bypass CSRF
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])  # Frontend domains allowed to access API




ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': env.db("DATABASE_URL")
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']


if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.authentication.CustomJWTAuthentication',   # JWT from cookies
        'rest_framework.authentication.SessionAuthentication',  # For admin/session
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your API Title',
    'DESCRIPTION': 'Optional description here',
    'VERSION': '1.0.0',
}




AUTH_USER_MODEL = 'users.User'
# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Access token expiry
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Refresh token expiry
    'AUTH_HEADER_TYPES': ('Bearer',),                # Accepted auth header
    'ROTATE_REFRESH_TOKENS': True,                   # Rotate refresh tokens
    'BLACKLIST_AFTER_ROTATION': True,                # Blacklist old tokens

    "AUTH_COOKIE": "access",                         # Access token cookie name
    "AUTH_COOKIE_REFRESH": "refresh",                # Refresh token cookie name
    "AUTH_COOKIE_SECURE": True,                      # Use HTTPS only
    "AUTH_COOKIE_HTTP_ONLY": True,                   # JS can't access
    "AUTH_COOKIE_PATH": "/",                         # Valid for all paths
    "AUTH_COOKIE_SAMESITE": "Lax",                   # CSRF protection
}
# Djoser settings
DJOSER = {
    "LOGIN_FIELD": "email",                                     # Login using email
    "USER_CREATE_PASSWORD_RETYPE": False,                       # No second password field
    "SEND_ACTIVATION_EMAIL": True,  # Activation email will be sent if is_active=False
    'ACTIVATION_URL': 'auth/activation/{uid}/{token}',

    "SERIALIZERS": {
        "user_create": "users.serializers.CustomUserCreateSerializer",  # Custom signup serializer
        "user": "users.serializers.CustomUserSerializer",               # Returned user serializer
        "current_user": "users.serializers.CustomUserSerializer",       # /me endpoint
    },
    "PASSWORD_RESET_CONFIRM_URL": "auth/reset_password_confirm/{uid}/{token}/",  # Reset link path
    "TOKEN_MODEL": None,                                        # Use JWT, not token model
    "JWT_AUTH_COOKIE": "access",                                # Access cookie name
    "JWT_AUTH_REFRESH_COOKIE": "refresh",                       # Refresh cookie name
}

# Site settings
DJANGO_ENV = env("DJANGO_ENV", default="local")

if DJANGO_ENV == "production":
    SITE_ID = 1
    DOMAIN = "cadworkbridge.com"
    SITE_NAME = "CadworkBridge"

elif DJANGO_ENV == "FlyPreview":
    SITE_ID = 2
    DOMAIN = "cadworkbridge.fly.dev"
    SITE_NAME = "FlyPreview"

elif DJANGO_ENV == "local":
    SITE_ID = 3
    DOMAIN = "localhost:8000"
    SITE_NAME = "LocalDev"




# Cloudinary settings
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': env("CLOUDINARY_API_KEY"),
    'API_SECRET': env("CLOUDINARY_API_SECRET"),
}

# Allauth settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*"]
LOGIN_REDIRECT_URL = "/auth/session-to-jwt/"
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': '',
        },
        "SCOPE": ["profile","email",],
        "AUTH_PARAMS": {"access_type": "online",},
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_SMTP_MODE = env("EMAIL_SMTP_MODE", default="GMAIL")

if EMAIL_SMTP_MODE == "GMAIL":
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = env("GMAIL_EMAIL_USER")
    EMAIL_HOST_PASSWORD = env("GMAIL_EMAIL_PASSWORD")
    DEFAULT_FROM_EMAIL = 'CadworkBridge <cadworkbridge@gmail.com>'
elif EMAIL_SMTP_MODE == "BREVO":
    EMAIL_HOST = 'smtp-relay.brevo.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = env("BREVO_EMAIL_USER")
    EMAIL_HOST_PASSWORD = env("BREVO_EMAIL_PASSWORD")
    DEFAULT_FROM_EMAIL = 'CadworkBridge <cadworkbridge@gmail.com>'