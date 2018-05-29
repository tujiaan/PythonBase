from producer.ext import mqtt
from producer.mqtt.handles import gateway_info
from web.models import *


def mqtt_register():
    # topics = Topic.query.with_entities(Topic.name).all()
    # for topic in topics:
    #     mqtt.subscribe(topic=topic, qos=2)
    #     task_name = topic.task_name

     mqtt.subscribe('gatewayinfo')
     mqtt.client.message_callback_add('gatewayinfo', gateway_info)