from celery import Celery

from .mqtt import mqtt
# celery = Celery('tasks', broker='redis://127.0.0.1:6379/0')
celery = Celery('tasks', broker='pyamqp://kaive:yangjiawei@36.1.52.72//')

def ext_init(app):
    mqtt.init_app(app)