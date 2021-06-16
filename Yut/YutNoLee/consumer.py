import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        try:
            message = text_data_json['message']
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        except:
            pass
        try:
            result = text_data_json['result']
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'Yut_result',
                    'result': result
                }
            )
        except:
            pass
        try:
            ID = text_data_json['ID']
            async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'ID_message',
                'ID': ID
            }
        )
        except:
            pass



    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    # Receive message from room group
    def Yut_result(self, event):
        result = event['result']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'result': result
        }))

    def ID_message(self, event):
        ID = event['ID']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'ID' : ID
        }))