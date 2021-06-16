from .wsgi import *
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from YutNoLee import routing
#from Yut.YutNoLee import routing
# 뭐지시발 왜 경로가 안맞게 해야 되는거지

application = ProtocolTypeRouter({
    # (http->django views is added by default)
     'websocket': AuthMiddlewareStack(
         URLRouter(
            routing.websocket_urlpatterns
         )
    ),
})
