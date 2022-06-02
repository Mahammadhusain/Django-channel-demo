from django.urls import path
from .consumer import NotificationClass


websocket_urlpatterns = [
    path('ws/sc/', NotificationClass.as_asgi()),
]
