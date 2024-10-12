from sys import argv

from shop.base import *

SECRET_KEY = config("SECRET_KEY", cast=str)

TESTING = 'test' in argv
if not TESTING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        'debug_toolbar',

    ]
    MIDDLEWARE = [
        *MIDDLEWARE,
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "django_shop",
        "USER": "postgres",
        "PASSWORD": "postgres",
        'HOST': "localhost"
    }
}


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
