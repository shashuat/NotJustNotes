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

        self.transcript = ""
        self.summary = ""

        
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

        self.transcript += script

        contents = {
                "d_type": "lyrics_para",
                "d_text": script
                }

        self.send(text_data = json.dumps(contents))

    def beg_script(self, event):
        self.transcript = event["trans"]
        self.summary = event["summary"]

        contents = {
                "teach_class": event["teach_class"],
                "teach_time": event["teach_time"],
                "teach_er": event["teach_er"],
                }

        for k,v in contents.items():
            self.send(text_data = json.dumps(
                {
                    "d_type" : k,
                    "d_text" : v,
                    }))
            


     


        

