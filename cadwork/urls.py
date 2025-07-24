from django.urls import path
from .views import Addition,CadworkTestApi

app_name = 'cadwork'
urlpatterns = [
    path('addition/', Addition.as_view(), name='addition'),
    path('cadwork_test_api/', CadworkTestApi.as_view(), name='cadwork-test-api'),
]