import flask_restplus

from producer.views import api_v1_bp as api_bp
api = flask_restplus.Api(api_bp,
                         title="消防API",
                         description="API",
                         contact="Tianjin Huitong Technology Co., Ltd",
                         contact_email="support@huitong-tech.com",
                         version="1.0", )
from .mqtt import api as mqtt_ns
api.add_namespace(mqtt_ns,path='/mqtt')