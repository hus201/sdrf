# Simple Django Rest Framework

Simple Django Rest Framework is django based app used to provide abstraction that combines both django rest framework with drf_yasg a swagger generator to implement good looking and  well documented apis using djang


## Quick Start

### Install
1. assuming you already have a django project that you need to add this app to you need to start with installing the package using
```
pip install sdrf
```
2. install required apps to INSTALLED_APPS in django settings
```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "drf_yasg",
    'sdrf',
]
```
3. add swagger docs url to your project urls
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    ...
    path('',include('sdrf.urls'))
]
```
4. check out if everything is okay by visting default swagger docs url at ``http://<your-project-url>/rest``
![Empty Swagger UI example](docs/empty-swagger-ui.png)

### Configure

### Build API Endpoints


