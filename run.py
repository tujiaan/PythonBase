#!/usr/bin/python3
# coding: utf-8
from web import create_app

application = create_app()
if __name__ == '__main__':
    application.run(host="127.0.0.1", port=5003, threaded=True)
