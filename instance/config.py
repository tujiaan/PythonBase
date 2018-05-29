import os
import platform

from celery.schedules import crontab

DEBUG = False

# System
VERSION = '1.0.0'
OS = platform.system()
DIR = os.getcwd()
redis = os.environ.get('REDIS_URI', 'redis://192.168.0.188:6379/')
##APP
# SESSION_COOKIE_SECURE=True
SECRET_KEY = 'mY@Ccrzx4v&U4yPGv2pXTWDK8skvTE5Z'

# BASE_URL = 'https://tw.woody.vip'
BASE_URL = 'https://www.eykszx.cn'

##CSRF
WTF_CSRF_ENABLED = False

##Sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:root@127.0.0.1:3306/firefighting')
# SQLALCHEMY_DATABASE_URI= 'postgresql+pg8000://kaive@127.0.0.1/yiyiwei'
#SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/1.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

##Redis

REDIS_URL = redis + '0'

##Cache
CACHE_TYPE = 'redis'
CACHE_REDIS_URL = redis + '1'

# Restplus
RESTPLUS_MASK_SWAGGER = False

RESTPLUS_MASK_HEADER = 'jwt1'
SWAGGER_UI_JSONEDITOR = False
SWAGGER_UI_LANGUAGES = ['zh-cn']

# Babel
BABEL_DEFAULT_LOCALE = 'zh_CN'

# JWT
JWT_PK = DIR + '/instance/jwt_rsa_private_key.pem'
JWT_PUK = DIR + '/instance/jwt_rsa_public_key.pem'
JWT_EXP = 60 * 60 * 24 * 30
JWT_NBF = 60

# Cors
CORS_RESOURCES = {r"/api/*": {"origins": "*"}}


# MQTT
MQTT_BROKER_URL = '127.0.0.1'
MQTT_BROKER_PORT = 1883
MQTT_USERNAME = 'admin'
MQTT_PASSWORD = 'public'
MQTT_KEEPALIVE = 60
MQTT_TLS_ENABLED = False
MQTT_LAST_WILL_QOS = 2

# Celery
CELERY_BROKER_URL = 'redis://192.168.0.188:6379/0',
CELERY_RESULT_BACKEND = 'redis://192.168.0.188:6379/1'
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERYBEAT_SCHEDULE = {
#     'every-15-min-at-8-to-22': {
#         'task': 'express.update',
#         'schedule': crontab(minute='*/15', hour='8-22')
#     },
#     'every-1-hour': {
#         'task': 'access_token.update',
#         'schedule': crontab(minute=0, hour='*/1')
#     },
#     'every-9-am': {
#         'task': 'library.return_books',
#         'schedule': crontab(minute=0, hour='9')
#     }
# }
#prefix
PREFIX='47.91.222.196:18083'
