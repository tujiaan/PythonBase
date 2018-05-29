import json
from producer.ext import celery
from web.models import Task, Topic


def gateway_info(client, userdata, message):
    p = json.loads(message.payload)
    topic_name = message.topic
    topic = Topic.query.filter(Topic.task_name == topic_name).first()
    print("!!!!")
    celery.send_task(topic.task_name, [p])


def gateway_data(client, userdata, message):
    # p = json.loads(message.payload)
    # print(p)

    pass