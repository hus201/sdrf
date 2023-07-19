from django.urls import path
from sdrf.swagger_config import schema_view
from django.conf import settings
from sdrf.utils.settings_utils import get_settings_value
REST_BASE_URL = get_settings_value('REST_APP_BASE_URL','rest')

urlpatterns = [
    path(f'{REST_BASE_URL}',
         schema_view.with_ui('swagger', cache_timeout=0),
         name="schema-swagger-ui")
]
