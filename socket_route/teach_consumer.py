import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from route.models import course  

from asgiref.sync import sync_to_async 
import whisper

from datetime import datetime


from tldr import getSummary
from tldr.getSummary import getSummary


class TeachConsumer(AsyncWebsocketConsumer):
     async def connect(self):
        await self.accept()
        self.user = self.scope["user"]
        self.route = self.scope["path"]
        
        self.class_id = self.route.split("/")[-1]

        self.caller = 0
        self.header = []
        self.head_size = 256

        self.transcript = ""
        self.summary = ""
        self.chunks = []

        self.start_time = datetime.now().strftime("%H:%M:%S")
        self.narration = True

        await self.channel_layer.group_add(f"class-{self.class_id}-teacher", self.channel_name)
        await self.channel_layer.group_add(f"class-{self.class_id}-joined", self.channel_name)

        data = await sync_to_async(course.objects.get)(course_id=self.class_id)
        self.class_name = data.course_name

        await self.channel_layer.group_send(
            f"class-{self.class_id}-student",
            {
                "type": "class_started",
                "class_id": self.class_id,
                "course_name": data.course_name
            },
        )

        set_con = {
                "teach_class": self.class_name,
                "teach_time": self.start_time,
                "teach_er" : f"{self.user}"
                }

        await self.channel_layer.group_send(
                f"class-{self.class_id}-teacher",
                { 
                    "type": "disp",
                    "contents": set_con
                }
         )


        self.model = whisper.load_model("tiny")

    #    await self.channel_layer.group_send(f"class-{self.class_id}-teacher", {
    #       "type" : "summ"
    #       })


     async def receive(self, bytes_data):
        if len(bytes_data) < 10:
            await self.channel_layer.group_send(
                    f"class-{self.class_id}-joined",
                    {
                        "type": "summ",
                        })
        else: 
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


            await self.channel_layer.group_send(
                    f"class-{self.class_id}-joined",
                    {
                        "type": "transcription",
                        "trans": script ,
                        },)
            


     async def send_script(self, event):
        await self.channel_layer.send(f"{event['sender']}",
            {
                "type" : "beg_script",
                "trans" : self.transcript,
                "summary" : self.summary,
                "teach_er" : f"{self.user}",
                "teach_class": self.class_name,
                "teach_time" : self.start_time
                
                })

     async def transcription(self, event):
        script = event["trans"]

        contents = {
                "d_type": "lyrics_para",
                "d_text": script}


        await self.send(text_data = json.dumps(contents))

     async def disp(self, event):
        contents = event["contents"]
        
        for k,v in contents.items():
            await self.send(text_data = json.dumps(
                {
                    "d_type" : k,
                    "d_text" : v,
                    }))

     async def summ(self, event):
            self.summary = getSummary(self.transcript)

            if not self.summary == "":
                await self.channel_layer.group_send(f"class-{self.class_id}-joined",
                        {
                            "type": "narrate",
                            "summary": self.summary
                            })

     async def narrate(self, event):
            self.summary = event["summary"]

            await self.send(text_data = json.dumps(
                {
                    "d_type" : "summary_para",
                    "d_text" : self.summary
                    }))











