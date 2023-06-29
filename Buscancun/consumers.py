import json
from apps.chofer.models import Autobus
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class MyConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = 'sala_unica'

        # Unirse al grupo de la sala
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
        await self.get_new_data()


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


    # Función para obtener nuevos datos en tiempo real
    async def get_new_data(self):
        print('ejecutado')
        # Obtén los nuevos datos de tu modelo
        new_data = Autobus.obtener_autobuses_activos()  # Agrega tu lógica de filtrado si es necesario
        # new_data = await Autobus.obtener_autobuses_activos()
        print(new_data)
        # Convierte los nuevos datos en un formato adecuado para el envío
        formatted_data = []  # Formatea los datos según tus necesidades

        # Envia los nuevos datos a los clientes suscritos
        # async_to_sync(self.channel_layer.group_send)("sala_unica", {"type": "send_message", "message": formatted_data})
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send_message',
                'message': json.dumps({'dato1':formatted_data})
            }
        )

    async def send_message(self, event):
        # Enviar mensaje a todos los clientes en la misma sala
        message = event['message']
        await self.send(text_data=message)


class NewDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Conexión WebSocket establecida
        await self.accept()

        # Suscribir al grupo de actualizaciones de nuevos datos
        async_to_sync(self.channel_layer.group_add)("new_data_updates", self.channel_name)

    async def disconnect(self, close_code):
        # Desuscribir del grupo de actualizaciones de nuevos datos
        async_to_sync(self.channel_layer.group_discard)("new_data_updates", self.channel_name)

    async def send_new_data(self, event):
        # Enviar nuevos datos a los clientes
        await self.send(json.dumps(event['data']))

    # Función para obtener nuevos datos en tiempo real
    def get_new_data(self):
        # Obtén los nuevos datos de tu modelo
        new_data = TuModelo.objects.filter(...)  # Agrega tu lógica de filtrado si es necesario

        # Convierte los nuevos datos en un formato adecuado para el envío
        formatted_data = [...]  # Formatea los datos según tus necesidades

        # Envia los nuevos datos a los clientes suscritos
        async_to_sync(self.channel_layer.group_send)("new_data_updates", {"type": "send_new_data", "data": formatted_data})
