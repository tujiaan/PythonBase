from flask_restplus import Resource, abort
from flask_restplus.reqparse import RequestParser

from web.ext import db
from web.models import Topic, List
from . import api
topic_parser = RequestParser()
topic_parser.add_argument('gateway_id', type=str, required=True, location='form')
topic_parser.add_argument('name', type=str, required=True, location='form')
topic_parser.add_argument('type', type=int, required=True, location='form')
topic_parser.add_argument('format', type=str, required=True, location='form')
topic_parser.add_argument('if_zip', type=str, required=True, location='form')
topic_parser.add_argument('note', type=str, required=True, location='form')
topic_parser.add_argument('state', type=str, required=True, location='form')


class TopicsView(Resource):
    @api.doc('新增主题')
    @api.expect(topic_parser, validate=True)
    def post(self):
        topic = Topic()
        args = topic_parser.parse_args()
        topic.type = args['type']
        topic.name = args['name']
        topic.gateway_id = args['gateway_id']
        topic.note = args['note']
        if args['type'] == 1:
            topic.format = args['gateway_id']+'/data/'+args['formate']
        else: topic.format = args['gateway_id']+'/cmd/'+args['formate']
        topic.if_zip = args['if_zip']
        topic.state = args['state']####从平台上拿数据
        topic.add()


class TopicView(Resource):
    @api.doc('删除主题')
    def delete(self,id):
        topic = Topic.query.filter(Topic.state ==1).filter(Topic.id ==id).first()
        if topic:
            topic.state=0
        else:abort(404)


class TopicListView(Resource):
    @api.doc('配置主题')
    def post(self, listid, topicid):
        topic = Topic.query.filter(Topic.state ==1).filter(Topic.id ==topicid).first()
        list = List.query.filter(List.state ==1).filter(List.id ==listid).first()
        if topic and list:
            topic.list.append(list)
            db.session.commit()
        else:abort(404)


