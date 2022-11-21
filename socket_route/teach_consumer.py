import json
from channels.generic.websocket import WebsocketConsumer
from route.models import course  

from asgiref.sync import async_to_sync
import whisper

class TeachConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.user = self.scope["user"]
        self.route = self.scope["path"]
        
        self.class_id = self.route.split("/")[-1]

        self.caller = 0
        self.header = []
        self.head_size = 256

        self.transcript = ""
        self.summary = ""
        self.chunks = []

        async_to_sync(self.channel_layer.group_add)(f"class-{self.class_id}-teacher", self.channel_name)
        async_to_sync(self.channel_layer.group_add)(f"class-{self.class_id}-joined", self.channel_name)

        data = course.objects.get(course_id=self.class_id)
        self.class_name = data.course_name

        async_to_sync(self.channel_layer.group_send)(
            f"class-{self.class_id}-student",
            {
                "type": "class_started",
                "class_id": self.class_id,
                "course_name": data.course_name
            },
        )

        set_con = {
                "teach_class": self.class_name,
                "teach_time": "00:00:00",
                "teach_er" : f"{self.user}"
                }

        async_to_sync(self.channel_layer.group_send)(
                f"class-{self.class_id}-teacher",
                { 
                    "type": "disp",
                    "contents": set_con
                }
         )



        self.model = whisper.load_model("tiny")


    def receive(self, bytes_data):
        self.chunks.append(bytes_data)

        filename = f'samples/filename{self.caller}.mp3'

        bd  = bytearray(bytes_data)

        if self.caller == 0:
            self.header = bd[0:self.head_size]
        else:
            new_head = bytearray(256)

            new_head[:] = self.header
            new_head.extend(bd)

            bytes_data = bytes(new_head)



        data = open(filename, 'wb')
        data.write(bytes_data)
        data.close()

        
        self.caller = self.caller + 1

        trans = self.model.transcribe(filename)
        script = trans['text']


        self.transcript += script


        async_to_sync(self.channel_layer.group_send)(
                f"class-{self.class_id}-joined",
                {
                    "type": "transcription",
                    "trans": script ,
                    },)

    def send_script(self, event):
        async_to_sync(self.channel_layer.send)(f"{event['sender']}",
            {
                "type" : "beg_script",
                "trans" : self.transcript,
                "summary" : self.summary,
                "teach_er" : f"{self.user}",
                "teach_class": self.class_name,
                "teach_time" : "00:00:00"
                
                })


    def transcription(self, event):
        script = event["trans"]

        contents = {
                "d_type": "lyrics_para",
                "d_text": script}


        self.send(text_data = json.dumps(contents))

    def disp(self, event):
        contents = event["contents"]
        
        for k,v in contents.items():
            self.send(text_data = json.dumps(
                {
                    "d_type" : k,
                    "d_text" : v,
                    }))

