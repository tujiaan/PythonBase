#!/usr/bin/python3
# coding: utf-8
from flask import Flask
#app = Flask(__name__)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    with app.app_context():
        from producer.ext import ext_init
        ext_init(app)
        from producer.views import api_v1_bp
        app.register_blueprint(api_v1_bp)
        from producer.mqtt import mqtt_register
        mqtt_register()
        return app
