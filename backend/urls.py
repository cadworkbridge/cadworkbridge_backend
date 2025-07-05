from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include(('authentication.urls','authentication'), namespace='authentication')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('auth/', include(('djoser.urls', 'djoser'), namespace='djoser')),# Djoser main user endpoints
    path('auth/', include(('djoser.urls.jwt', 'jwt'), namespace='jwt')),# Djoser JWT endpoints

    # Social login URLs (Google logi
]



# =================== DJOSER STANDARD ENDPOINTS (namespace='djoser') ===================

# path('auth/users/', ...)
#   Method: POST
#   Reverse Name: djoser:user-list
#   Task: Register a new user

# path('auth/users/me/', ...)
#   Method: GET, PATCH, DELETE
#   Reverse Name: djoser:user-me
#   Task:
#     - GET: Get current user info
#     - PATCH: Update current user data
#     - DELETE: Delete own account

# path('auth/users/set_password/', ...)
#   Method: POST
#   Reverse Name: djoser:user-set-password
#   Task: Change password (authenticated)

# path('auth/users/reset_password/', ...)
#   Method: POST
#   Reverse Name: djoser:password-reset
#   Task: Request password reset email

# path('auth/users/reset_password_confirm/', ...)
#   Method: POST
#   Reverse Name: djoser:password-reset-confirm
#   Task: Confirm new password with UID + token


# =================== DJOSER JWT ENDPOINTS (namespace='jwt') ===================

# path('auth/jwt/create/', ...)
#   Method: POST
#   Reverse Name: jwt:jwt-create
#   Task: Login (obtain access + refresh tokens)

# path('auth/jwt/refresh/', ...)
#   Method: POST
#   Reverse Name: jwt:jwt-refresh
#   Task: Get a new access token from refresh token

# path('auth/jwt/verify/', ...)
#   Method: POST
#   Reverse Name: jwt:jwt-verify
#   Task: Verify if access token is valid

# path('auth/jwt/logout/', ...)
#   Method: POST
#   Reverse Name: jwt:jwt-logout
#   Task: Invalidate (blacklist) refresh token and log out user
