from django.urls import path
from srf.swagger_config import schema_view
from django.conf import settings

urlpatterns = [
    path(f'{settings.REST_APP_BASE_URL}/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name="schema-swagger-ui")
]
