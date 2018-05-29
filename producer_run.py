#!/usr/bin/python3
# coding: utf-8
from producer import create_app

application = create_app()
if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5006, threaded=True)
