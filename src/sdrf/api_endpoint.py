from abc import ABC, abstractmethod

from django.urls import path
from django.utils.decorators import classonlymethod
from rest_framework.request import Request
from rest_framework.response import Response
from sdrf.endpoint_config import APIEndpointConfig
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from sdrf.enums import ParameterType, APIParamDataType
from rest_framework.decorators import permission_classes, authentication_classes


class APIEndpoint(ABC):

    ParameterTypes = ParameterType
    DataType = APIParamDataType

    @classonlymethod
    @abstractmethod
    def configure(self, config: APIEndpointConfig) -> APIEndpointConfig:
        pass

    @classonlymethod
    def as_url(self):
        config: APIEndpointConfig = APIEndpointConfig(name=self.__name__)
        config = self.configure(self, config)
        assert config.endpoint != '' or config.full_route != '', 'you need to setup either endpoint or full route'
        authorized_function = permission_classes(config.permission_classes)(self.execute)
        authenticated_function = authentication_classes(config.authentication_classes)(authorized_function)
        as_view = api_view([config.http_method])(authenticated_function)
        with_swagger = swagger_auto_schema(
            name=config.name,
            operation_description=config.description,
            operation_summary=config.summary,
            deprecated=config.deprecated,
            method=config.http_method,
            manual_parameters=config.parameters,
            request_body=config.request_body,
            responses=config.responses,
            tags=config.tags
        )(as_view)
        url = path(config.get_full_route(), with_swagger, name=config.name)
        return url

    @staticmethod
    @abstractmethod
    def execute(request: Request, *args, **kwargs) -> Response:
        pass
