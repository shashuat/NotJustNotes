from django.urls import re_path
from . import dash_consumer
from . import teach_consumer
from . import class_consumer

websocket_urlpatterns = [
        re_path(r'ws/teach/', teach_consumer.TeachConsumer.as_asgi()),
        re_path(r'ws/dash/', dash_consumer.DashConsumer.as_asgi()),
        re_path(r'ws/class/', class_consumer.ClassConsumer.as_asgi())
        ]

