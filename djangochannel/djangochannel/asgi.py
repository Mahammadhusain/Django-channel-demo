import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter #---------> this (3)
from myapp.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochannel.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({ #---------> this (4)
    'http':get_asgi_application(), #---------> For Normal http Request
    'websocket':URLRouter(websocket_urlpatterns), #---------> For Web-Socket Request
})
