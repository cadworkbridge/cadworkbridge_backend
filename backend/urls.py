from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('cards/', include(('cards.urls', 'cards'), namespace='cards')),
    path('cadwork/', include(('cadwork.urls', 'cadwork'), namespace='cadwork')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/', include('allauth.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),# OpenAPI schema (JSON)
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),# Swagger UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),# Redoc UI (optional)

]


