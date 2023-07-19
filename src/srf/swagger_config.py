from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
APP_TITLE = settings.REST_APP_NAME if settings.REST_APP_VERSION is not None else 'Weather API'
APP_VERSION = settings.REST_APP_VERSION if settings.REST_APP_VERSION is not None else 'v1'
APP_CREATOR = {
    'name': '',
    'email': '',
    'url': ''
}
if settings.REST_APP_CREATOR is not None:
    APP_CREATOR.update(settings.REST_APP_CREATOR)

APP_CREATOR_CONTACT = openapi.Contact(
    name=APP_CREATOR['name'],
    email=APP_CREATOR['email'],
    url=APP_CREATOR['url']
)

schema_view = get_schema_view(
    openapi.Info(
        title=settings.REST_APP_NAME,
        default_version=settings.REST_APP_VERSION,
        contact=APP_CREATOR_CONTACT,
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

