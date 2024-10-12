"""
WSGI config for shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from decouple import config


from django.core.wsgi import get_wsgi_application


debug_mode = config("DEBUG", cast=bool, default=True)

if debug_mode:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings.production')

application = get_wsgi_application()
