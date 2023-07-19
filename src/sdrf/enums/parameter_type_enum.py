from enum import Enum
from drf_yasg.openapi import IN_HEADER, IN_BODY, IN_FORM, IN_PATH, IN_QUERY


class ParameterType(Enum):
    HEADER_PARAM = IN_HEADER
    BODY_PARAM = IN_BODY
    PATH_PARAM = IN_PATH
    QUERY_PARAM = IN_QUERY
    FORM_PARAM = IN_FORM
