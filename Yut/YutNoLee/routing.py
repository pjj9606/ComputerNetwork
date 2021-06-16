# chatapp/routing.py
from django.urls import re_path
from django.conf.urls import url

from . import consumer

websocket_urlpatterns = [
    url(r'ws/chat/(?P<room_name>[^/]+)/$', consumer.ChatConsumer.as_asgi()),
    #re_path(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
]
