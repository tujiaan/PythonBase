from celery import Celery

# app = Celery('tasks', broker='redis://127.0.0.1:6379/0')
# from celery.utils.log import get_task_logger

celery = Celery('tasks', broker='redis://192.168.0.188:6379/0')
#celery.conf.update(app.'config.py')
# logger = get_task_logger(__name__)


@celery.task(bind=True, name='test.add')
def add(self, p):
   print(p)