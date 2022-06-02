from email import message
from channels.consumer import SyncConsumer,AsyncConsumer,StopConsumer
import asyncio




# ------------ SyncConsumer (Handle all request one by one) -------------------
# class MySyncConsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print('Connected')
#     def websocket_receive(self,event):
#         print('Received')
#     def websocket_disconnect(self,event):
#         print('Disconnected')


# ------------ AsyncConsumer (Handle all request simultaneously) -------------------
# class MyAsyncConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print('Connected',event)
#         await self.send({ # ----------> Accept connection Server 
#             "type": "websocket.accept",
#         })
    

#     async def websocket_receive(self,event):
#         print('Received',event)
#         for i in range(30):
#             await self.send({
#                 "type": "websocket.send", # ----------> Server can send message to client
#                 "text": f'{i}', # ----------> Server Message to client
#             })
#             await asyncio.sleep(1) # ----------> Recive message After 1sec.
#     async def websocket_disconnect(self,event):
#         print('Disconnected',event)
#         raise StopConsumer() # ----------> Stop Connection safely Between (client-server)

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------


from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class NotificationClass(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'test_notify'
        self.room_group_name = 'test_notify_group'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({'status':'Connected success'}))

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status':'Received success '}))

    async def disconnect(self, *args, **kwargs):
        print('Disconnected success')


    async def send_notification(self,event):
        print('********** Notification ***********')
        data = json.loads(event.get('value'))
        print('********** Notification ***********')
        await self.send(text_data=json.dumps({'payload':data}))