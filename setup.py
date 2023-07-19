from setuptools import setup

setup(
    name='srf',
    version='0.0.1',
    author='Hussein Anabtawi',
    description='Simple rest framework an abstraction that combines django rest framework with drf_yasg ',
    long_description='Simple rest framework is an abstraction for building rest api with well written documentations ',
    url='https://github.com/BenjaminFranline',
    keywords='django, rest apis, abstraction',
    python_requires='>=3.8, <4',
    install_requires=[
        'Django>=4.1.3',
        'djangorestframework~=3.14.0',
        'drf_yasg'
    ],

)