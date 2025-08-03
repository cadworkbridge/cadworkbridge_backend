from django.contrib import admin
from django.urls import path, include
from users.views import VerifyActivationView, SocialAuthCompleteView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/verify-activation/', VerifyActivationView.as_view(), name='verify_activation'),  # Your new endpoint
    path('', include(('core.urls', 'core'), namespace='core')),
    path('bridge/', include(('bridge.urls', 'bridge'), namespace='bridge')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/complete/', SocialAuthCompleteView.as_view(), name='social-complete'),

]
