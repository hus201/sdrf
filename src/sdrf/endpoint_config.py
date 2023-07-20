from typing import Literal, List, Union, Dict, Type
from drf_yasg.openapi import Parameter, Schema, Response
from sdrf.enums import ParameterType, APIParamDataType
from rest_framework.serializers import Serializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.conf import settings
from sdrf.utils.settings_utils import get_settings_value

class APIEndpointConfig:
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.parameters = []
        self.tags = []
        self.responses = {}
        self.permission_classes = []
        self.authentication_classes = []

    name: str
    description: str = ''
    summary: str = ''
    http_method: Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] = 'GET'
    parameters: List[Parameter] = []
    responses: Dict = {}
    tags: List[str] = []
    request_body: Schema = None
    base_url: str = get_settings_value('REST_APP_BASE_URL','rest/')
    rest_api_version = get_settings_value('REST_APP_VERSION','v1')
    endpoint: str = ''
    full_route: str = ''
    deprecated: bool = False
    authentication_classes: List = []
    permission_classes: List = []

    def require_authenticated_permission(self):
        self.add_permission_class(IsAuthenticated)

    def add_permission_class(self, permission_class):
        assert issubclass(permission_class, BasePermission), 'Permission Class should be of type BasePermission'
        self.permission_classes.append(permission_class)

    def add_authentication_class(self, authentication_class):
        assert issubclass(authentication_class, BaseAuthentication), 'Permission Class should be an instance of ' \
                                                                     'BaseAuthentication '
        self.authentication_classes.append(authentication_class)

    def add_parameter(self,
                      name: str,
                      data_type: APIParamDataType = APIParamDataType.STRING,
                      parameter_type: ParameterType = ParameterType.QUERY_PARAM,
                      description: str = '',
                      required: bool = True,
                      default=None):
        if parameter_type.value == ParameterType.BODY_PARAM.value:
            if self.request_body is None:
                self.request_body = Schema(type=APIParamDataType.OBJECT.value, required=[], properties={})
            self.request_body.properties[name] = Schema(type=data_type.value)
            if required:
                self.request_body.required.append(name)

        else:
            param = Parameter(name=name,
                              description=description,
                              in_=parameter_type.value,
                              type=data_type.value,
                              required=required,
                              default=default)
            self.parameters.append(param)

    def add_tag(self, tag: str):
        tags = self.tags
        tags.append(tag)
        new_tags = list(set(tags))
        self.tags = new_tags

    def set_response(self, code: int, response: Union[Type[Serializer], str, Dict]):
        if response is Type[Serializer]:
            response = Response('', response)
        self.responses[code] = response

    def get_path_param_converter(self, param_type: str) -> str:
        rules = {
            APIParamDataType.STRING.value: 'str',
            APIParamDataType.INTEGER.value: 'int'
        }
        return rules[param_type]

    def get_full_route(self) -> str:
        if self.full_route != '':
            return self.full_route
        if self.base_url.endswith('/'):
            base_url = self.base_url[:-1]
        else:
            base_url = self.base_url
        full_route = f'{base_url}/{self.rest_api_version}/{self.endpoint}'
        path_parameters = [param for param in self.parameters if param.in_ == ParameterType.PATH_PARAM.value]
        for param in path_parameters:
            full_route = full_route + f'/<{self.get_path_param_converter(param.type)}:{param.name}>'
        return full_route
