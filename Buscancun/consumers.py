import json

from apps.chofer.api.serializers import AutobusSerializer
from apps.chofer.models import Autobus
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from apps.chofer.views import get_autobuses

from djangochannelsrestframework.decorators import action
from djangochannelsrestframework import permissions
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin
)


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
        # Obtén los nuevos datos de tu modelo
        new_data = sync_to_async(get_autobuses)()  # Agrega tu lógica de filtrado si es necesario
        # new_data = await Autobus.obtener_autobuses_activos()
        resultado = await new_data
        print(resultado)
        # Convierte los nuevos datos en un formato adecuado para el envío
        formatted_data = []  # Formatea los datos según tus necesidades

        # Envia los nuevos datos a los clientes suscritos
        # async_to_sync(self.channel_layer.group_send)("sala_unica", {"type": "send_message", "message": formatted_data})
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'send_message',
                'message': json.dumps(resultado)
            }
        )

    async def send_message(self, event):
        # Enviar mensaje a todos los clientes en la misma sala
        message = event['message']
        await self.send(text_data=message)


class AutobusConsumer(ListModelMixin, RetrieveModelMixin, PatchModelMixin, UpdateModelMixin, CreateModelMixin,
                      DeleteModelMixin, GenericAsyncAPIConsumer):
    queryset = Autobus.objects.all()
    serializer_class = AutobusSerializer

    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(AutobusSerializer.Meta.model)
    async def model_change(self, message, observer=None, *args, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=AutobusSerializer(instance=instance).data, action=action.value)
