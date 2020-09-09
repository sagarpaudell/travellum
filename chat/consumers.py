import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from accounts.models import User
from chat.models import Chat

from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope['user'].pk
        temp = self.scope['url_route']['kwargs']['email']
        temp2 = await sync_to_async(User.objects.get, thread_sensitive=True)(email=temp)
        self.friend_id = temp2.pk
        self.room_group_name = f'chat_between{self.friend_id}and{self.id}' if self.friend_id<self.id else f'chat_between{self.id}and{self.friend_id}' 
        print(self.room_group_name)
        
        #join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        #accept connection
        await self.accept()
        
    async def disconnect(self, close_code):
        #leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #receive message from Websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message=text_data_json['message']
        #save message
        await self.save_messages( message )
        #send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender' : self.scope['user'].email,
                'time'   : timezone.now().isoformat()
            }
        )
        
    #receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_messages(self, message):
        sender = User.objects.get(id=self.id)
        receiver = User.objects.get(id=self.friend_id)
        hello = Chat(sender=sender, receiver=receiver, message_text=message)
        hello.save()


