from flask_restplus import Namespace
api = Namespace('Topic', description='主题相关操作')

from web.views.api_v1.topic.topic import TopicsView, TopicView, TopicListView

api.add_resource(TopicsView, '/')
api.add_resource(TopicView, '/<id>/')
api.add_resource(TopicListView, '/<topicid>/<listid>')