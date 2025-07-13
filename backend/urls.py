from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include(('authentication.urls','authentication'), namespace='authentication')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/', include('allauth.urls')),

]