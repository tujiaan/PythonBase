from flask_restplus import Namespace

api = Namespace('Student', description='学生相关接口')

from .student import StudentView, StudentList

api.add_resource(StudentView, '/<id>/')
api.add_resource(StudentList, '/')
