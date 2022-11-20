import json
from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync

from route.models import course

class ClassConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.user = self.scope["user"]
        self.route = self.scope["path"]
        
        self.class_id = self.route.split("/")[-1]

        self.transcription = []

        
        async_to_sync(self.channel_layer.group_send)(
            f"class-{self.class_id}-teacher",
            {
                "type": "send_script",
                "sender": f"{self.channel_name}",
            },
        )

        async_to_sync(self.channel_layer.group_add)(f"class-{self.class_id}-joined", self.channel_name)

    def transcription(self, event):
        script = event["trans"]

        self.send(text_data=json.dumps(
            {
                "trans" : f"{script}"
            }))

    def beg_script(self, event):
        self.transcription = event["text"]


        

