from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from sdrf.utils.settings_utils import get_settings_value
class ModelEndPoint(viewsets.ModelViewSet):
    @classmethod
    def as_urls(cls):
        router = DefaultRouter()
        base_url: str = get_settings_value('REST_APP_BASE_URL','rest/')
        rest_api_version = get_settings_value('REST_APP_VERSION','v1')
        if base_url.endswith('/'):
            base_url = base_url[:-1]
        view_name= cls.get_view_name(cls()).split(' ')[0] + 's'
        router.register(view_name.lower(),cls)
        url = path(f'{base_url}/{rest_api_version}/',include(router.urls))
        return url



