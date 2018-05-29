from flask_restplus import Namespace
api = Namespace('User', description='用户相关操作')
from .user import UserView######还是有跨域问题(=.=##)
api.add_resource(UserView, '/<id>/')