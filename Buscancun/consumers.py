import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = 'sala_unica'

        # Unirse al grupo de la sala
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Recibir mensaje del cliente WebSocket
        # y enviarlo a todos los clientes en la misma sala
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send_message',
                'message': text_data
            }
        )

    async def send_message(self, event):
        # Enviar mensaje a todos los clientes en la misma sala
        message = event['message']
        await self.send(text_data=message)