"""
WSGI config for Alumni project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from channels.routing import ProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alumni.settings")

application = get_wsgi_application()
# developement_application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })
