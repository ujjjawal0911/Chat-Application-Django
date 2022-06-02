import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message
from room.models import Room


class ChatRoomConsumer(WebsocketConsumer):

    # A function to get username
    def get_username(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            return str(self.scope['user'])
        else:
            return str(self.scope['session']['username'])

    def connect(self):
        # Get the room name from the URL
        self.room_name = self.scope['url_route']['kwargs']['room_name'].lower()

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        # Accepting the connection
        self.accept()

        # Getting Previous Messages
        last_messages = []
        print(self.room_name)
        print('*****************')
        for msg in Message.last_15_messages(self, self.room_name):
            last_messages.append({
                'username': msg.author.username,
                'message': msg.message,
                'time': msg.timestamp.timestamp(),
            })

        # Send a message to set the username variable
        self.send(text_data=json.dumps({
            'type': 'connection_made',
            'username': self.get_username(),
            'last_messages': last_messages,
        }))

        # Sending Message to all users notifying that a user joined
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'notify',
                'username': self.get_username(),
                'message': 'joined the chatroom',
            }
        )

    # Notify Message Function
    def notify(self, event):
        type = event['type']
        username = event['username']
        message = event['message']

        self.send(text_data=json.dumps({
            'type': type,
            'username': username,
            'message': message,
        }))

    # Recieve Event
    def receive(self, text_data=None):
        # Convert the TextData string to JSON Format
        text_data_json = json.loads(text_data)

        # Extract the message from JSON Format
        username = text_data_json['username']
        message = text_data_json['message']

        # Message Saving
        if self.user.is_authenticated:
            msg = Message(author=self.user, room_associated=Room.objects.get(
                room_name=self.room_name), message=message)
            msg.save()

        # Sending the message to the specified group
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    def chat_message(self, event):
        type = event['type']
        message = event['message']
        username = event['username']

        self.send(text_data=json.dumps({
            'type': type,
            'message': message,
            'username': username,
        }))

    # Disconnect

    def disconnect(self, event):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'notify',
                'username': self.get_username(),
                'message': 'left the chatroom',
            }
        )
