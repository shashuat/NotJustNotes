import json
from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync

from route.models import student

class DashConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.user = self.scope['user']

        data = student.objects.filter(student_name = self.user)


        courses = [x.course_id.pk for x in data]

        for cid in courses:
            async_to_sync(self.channel_layer.group_add)(f"class-{cid}-dashboard", self.channel_name) 

        async_to_sync(self.channel_layer.group_add)(f"class-7-student", self.channel_name) 
        self.send(text_data = json.dumps({
            'msg' : 'Joined dashboard'
            }))


    def class_started(self, event):
        self.send(text_data=json.dumps({
            'msg' : f'{event["course_name"]} has started'
            }))

