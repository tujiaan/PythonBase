from flask import request
from flask_restplus import Resource, fields

from web.ext import db, cache, redis
from . import api

studend_input_model = api.model('StudentInputModel', {
    'name': fields.String(required=True, description='姓名'),
    'teacher_id': fields.Integer
})
studend_out_model = api.model('StudentOutModel', {
    'id': fields.String,
    'name': fields.String,
})
get_parser = api.parser()
get_parser.add_argument('name',
                        type=str,
                        help="按名称查询",
                        required=False,
                        location='args')


class StudentView(Resource):
    @api.doc('Modify Student')
    @api.expect(studend_input_model, validate=True)
    @api.marshal_with(studend_out_model, as_list=False)
    def put(self, id):
        s = Student.query.get_or_404(id)
        args = request.json
        s.name = args.get('name')
        t = Teacher.query.get(args.get('teacher_id'))
        if t:
            s.teachers.append(t)
        db.session.commit()
        return s

    @api.doc('Get Student')
    @api.marshal_with(studend_out_model, as_list=False)
    def get(self, id):
        s = Student.query.get_or_404(id)
        print(s.teachers.all())
        print(s.classroom)
        print(s.dog)
        print(s.classroom.students.all())
        redis.set('ssss', 'sadasdasd')
        print(redis.get('ssss'))
        return s

    @api.doc('Delete Student')
    def delete(self, id):
        s = Student.query.get_or_404(id)
        db.session.delete(s)
        db.session.commit()
        return None, 204


class StudentList(Resource):
    @api.doc('Add Student')
    @api.expect(studend_input_model, validate=True)
    @api.marshal_with(studend_out_model, as_list=False)
    def post(self):
        args = request.json
        s = Student(name=args.get('name'))
        t = Teacher.query.get(args.get('teacher_id'))
        if t:
            s.teachers.append(t)
        db.session.add(s)
        db.session.commit()
        return s, 201

    @api.doc('Get Students')
    @api.marshal_with(studend_out_model, as_list=True)
    @api.expect(get_parser, validate=True)
    @cache.cached(timeout=20)
    def get(self):
        s = Student.query
        args = get_parser.parse_args()
        if args.get('name'):
            s = s.filter(Student.name.like(f'%{args.get("name")}%'))
        return s.all()
