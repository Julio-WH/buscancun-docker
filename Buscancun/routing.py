from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    re_path(r'ws/$', MyConsumer.as_asgi()),
]