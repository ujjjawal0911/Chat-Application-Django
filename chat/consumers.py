from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        # Get the room name from the URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data=None):
        # Convert the TextData string to JSON Format
        text_data_json = json.loads(text_data)

        # Extract the message from JSON Format
        message = text_data_json['message']

        # Temp ID to differentiate Anonymous Users
        temp_id = text_data_json['temp_id']
        username = str(self.scope['user'])

        # Sending the message to the specified group
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'temp_id': temp_id,
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']

        # To differentiate Anonymous Users
        temp_id = event['temp_id']

        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'temp_id': temp_id,
        }))
