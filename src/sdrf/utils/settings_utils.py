from typing import Any
from django.conf import settings

def get_settings_value(variable_name: str, default : Any = None):
    try:
        return settings.__getattribute__(variable_name)
    except AttributeError:
        return default
