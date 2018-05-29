#!/usr/bin/python3
# coding: utf-8

from flask import Blueprint

from .api_v1 import api as api_v1

api_bp = Blueprint('cargo_api', __name__, url_prefix='/api/v1')


def register_view(app):
    api_v1.init_app(api_bp)
    app.register_blueprint(api_bp)
