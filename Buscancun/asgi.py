import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .routing import websocket_urlpatterns
from channels.http import AsgiHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Buscancun.settings')
django.setup()
application = ProtocolTypeRouter(
    {
        'http': AsgiHandler(),
        'websocket': URLRouter(websocket_urlpatterns),
    }
)
