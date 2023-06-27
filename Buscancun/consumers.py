import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print(self)
        await self.accept()
        # await self.send(text_data=json.dumps({
        #     'message': 'Conectadooo'
        # }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))


# class TestConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = "test_consumer"
#         self.room_group_name = "test_consumer_group"
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_name, self.room_group_name
#         )
#         self.accept()
#         self.send(text_data=json.dumps({'status':'Conectaddooooo'}))
