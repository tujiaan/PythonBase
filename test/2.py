from celery import Celery, app

celery = Celery('tasks',broker='redis://192.168.0.188:6379/0')



celery.send_task('consumer.add',[1,2])