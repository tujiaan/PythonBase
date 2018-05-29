from flask_restplus import Resource, abort
from flask_restplus.reqparse import RequestParser

from web.models import User
from .import api

user_parser = RequestParser()
user_parser.add_argument('password', type=str, required=True, location='form')


class UserView(Resource):
    @api.doc('修改用户密码')
    @api.expect(user_parser, validate=True)
    def put(self,id):
        user = User.query.filter(User.disabled==False).filter(User.id == id).first()
        if user:
            args = user_parser.parse_args()
            user.password = args['password']
            user.update()
        else:abort(404)

    @api.doc('删除用户')
    def delete(self, id):
        user = User.query.filter(User.disabled == False).filter(User.id == id).first()
        if user:
            user.delete()
        else:abort(404)
