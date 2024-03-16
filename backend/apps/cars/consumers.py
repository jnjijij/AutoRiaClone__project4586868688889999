from rest_framework.decorators import action

from backend.listings.models import CarModel
from backend.my_project.serializers import CarSerializer


class GenericAsyncAPIConsumer:
    pass


def model_observer(CarModel, serializer_class):
    pass


class CarConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.channel_layer = None
        self.channel_name = None
        self.scope = None
        self.room_name = 'cars'
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            print('ddddddddddddddddddddddddddddddddddddddddddd')
            await self.close()
            return
        await self.accept()
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

    @model_observer(CarModel, serializer_class=CarSerializer)
    async def cars_activity(self, message, action, subscribing_request_ids, **kwargs):
        for request_id in subscribing_request_ids:
            await self.reply(data=message, action=action, request_id=request_id)

    @action()
    async def subscribe_to_car_activity(self, request_id, **kwargs):
        await self.cars_activity.subscribe(request_id=request_id)

    def close(self):
        pass

    def accept(self):
        pass

    def reply(self, data, action, request_id):
        pass

    @classmethod
    def as_asgi(cls):
        pass