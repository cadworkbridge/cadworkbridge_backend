from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls','core'), namespace='core')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('auth/', include('djoser.urls')),         # ✅ Djoser main
    path('auth/', include('djoser.urls.jwt')),     # ✅ Djoser JWT under same path
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/social/', include('allauth.socialaccount.urls')),
]
