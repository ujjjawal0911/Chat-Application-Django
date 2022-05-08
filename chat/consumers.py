import json
from channels.generic.websocket import WebsocketConsumer


class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data=None):
        print('Message :', text_data)
        self.send(text_data=json.dumps({
            'message': 'Message Recieved'
        }))
