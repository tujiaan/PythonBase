import base64

from flask import request
from flask_restplus import Namespace, Resource
from flask_restplus.reqparse import RequestParser

from producer.ext import mqtt
api=Namespace('Mqtt',description='MQTT操作')




payload_parser=RequestParser()
payload_parser.add_argument('payload',help='社区名称',required=True,location='json')

@api.route('/')
class Command(Resource):
    @api.expect(payload_parser,validate=False)
    def post(self):
        data=request.data
        mqtt.publish('aaa',data)
        return ''
