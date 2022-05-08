import json
from channels.generic.websocket import WebsocketConsumer


class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'Established'
        }))
