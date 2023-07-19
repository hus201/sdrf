from django.urls import path
from sdrf.swagger_config import schema_view
from django.conf import settings
try:
    REST_BASE_URL = settings.REST_APP_BASE_URL
except AttributeError:
    REST_BASE_URL = 'rest'
urlpatterns = [
    path(f'{REST_BASE_URL}/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name="schema-swagger-ui")
]
