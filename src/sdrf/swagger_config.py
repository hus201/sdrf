from contextlib import suppress
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from sdrf.utils.settings_utils import get_settings_value
APP_TITLE = get_settings_value('REST_APP_NAME','Weather API')
APP_VERSION = get_settings_value('REST_APP_VERSION','v1')
APP_CREATOR = {
        'name': '',
        'email': '',
        'url': ''
    }
with suppress(AttributeError):
    APP_CREATOR.update(settings.REST_APP_CREATOR)

APP_CREATOR_CONTACT = openapi.Contact(
    name=APP_CREATOR['name'],
    email=APP_CREATOR['email'],
    url=APP_CREATOR['url']
)


schema_view = get_schema_view(
    openapi.Info(
        title=APP_TITLE,
        default_version=APP_VERSION,
        contact=APP_CREATOR_CONTACT,
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

