# 1- Install channels (pip install channel)
# 2- Registerd in django installed_app (setting.py)
  INSTALLED_APPS = [
    'channels', # <----------------- this
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 3- ASGI_APPLICATION = 'djangochannel.asgi.application' (setting.py)
# 4- Make consumer.py file in app 
# ---------- consumer.py ---------------
from channels.consumer import AsyncConsumer,StopConsumer
# ------------ AsyncConsumer -------------------
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event): # called at when client make connection
        print('Connected',event)
        await self.send({ # ----------> Accept connection Server
            "type": "websocket.accept",
        })
        

    async def websocket_receive(self,event): # called at when data recived form client
        print('Received',event) # client દ્વારા જે મેસેજ send કરવામાં આવે છે તે અહી event માં receive થશે.
    
        await self.send({
            "type": "websocket.send", # ----------> આ code દ્વારા server to client message કરી શકાય છે.
            "text": event["text"], # ----------> Message Body for do message (Server to Client)
        })

    async def websocket_disconnect(self,event): # called at when client or server terminate connection
        print('Disconnected',event)
        raise StopConsumer() # ----------> Stop Connection safely Between (client-server)

# 5- Make routing.py file in app 
# ---------- routing.py ---------------
from django.urls import path
from .consumer import MyAsyncConsumer


websocket_urlpatterns = [
    path('ws/sc/', MyAsyncConsumer.as_asgi()),
]

# 6- Do config in asgi.py 
# ---------- asgi.py ---------------
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter #---------> this (3)
from myapp.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochannel.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({ #---------> this (4)
    'http':get_asgi_application(), #---------> For Normal http Request
    'websocket':URLRouter(websocket_urlpatterns), #---------> For Web-Socket Request
})


