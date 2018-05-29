#!/usr/bin/python3
# coding: utf-8
from flask import Flask

from werkzeug.contrib.fixers import ProxyFix


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_pyfile('config.py')
    with app.app_context():
        from web.ext import ext_init
        ext_init(app)
        from web.views import register_view
        register_view(app)
    return app


def test():
    app = Flask(__name__, instance_relative_config=True)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_pyfile('config.py')
    with app.app_context():
        from web.ext import db
        db.init_app(app)
        from web.scripts import init_database
        init_database.init()
    return app
