# coding: utf-8

from bson import ObjectId

from web.ext import db


def objectid():
    return str(ObjectId())


t_topic_list = db.Table(
    'topic_list',
    db.Column('t_id', db.String(16), db.ForeignKey('topic.id')),
    db.Column('l_id', db.String(16), db.ForeignKey('list.id')),
    db.UniqueConstraint('t_id', 'l_id', name='unix_t_l')
)


class Gateway(db.Model):
    __tablename__ = 'gateway'
    gateway_id = db.Column(db.String(16), nullable=False, default=objectid, primary_key=True, unique=True, comment='网关id')
    username = db.Column(db.String(16), nullable=False, default=objectid, comment='用户名')
    password = db.Column(db.String(16), nullable=False, default=objectid, comment='用户密码')
    if_SSL = db.Column(db.Boolean, nullable=False, default=False, comment='')
    connect = db.Column(db.Integer, comment='0:离线，1：在线')
    state = db.Column(db.Integer, comment='0:禁用，1：启用')
    note = db.Column(db.Text, comment='备注')

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.String(16), nullable=False, default=objectid, primary_key=True, unique=True, comment='id')
    gateway_id = db.Column(db.String(16), db.ForeignKey('gateway.gateway_id'), comment='网关id')
    type = db.Column(db.Integer, comment='1:网关发布,2:网管订阅')
    name = db.Column(db.String(100), comment='网关主题')
    format = db.Column(db.Integer, comment='1:json,2:rawdata')
    if_zip = db.Column(db.Boolean, nullable=False, default=False, comment='是否压缩')
    state = db.Column(db.Integer, comment='0:禁用,1:启用')
    note = db.Column(db.Text, comment='备注')
    task_name = db.Column(db.String(24), db.ForeignKey('task.name'))
    list = db.relationship('List', secondary=t_topic_list, backref=db.backref('t_list', lazy='dynamic'), lazy='dynamic')

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(16), nullable=False, default=objectid, primary_key=True, unique=True, comment='id')
    name = db.Column(db.String(24), comment='用户姓名')
    username = db.Column(db.String(24), comment='用户姓名')
    password = db.Column(db.String(24), comment='密码')
    email = db.Column(db.String(30), comment='邮箱')
    phone = db.Column(db.String(30), comment='电话')
    register_time = db.Column(db.DateTime, comment='注册时间')
    last_login = db.Column(db.DateTime, comment='上次登陆时间')
    app_key = db.Column(db.String(50), comment='AppKey')
    secret_key = db.Column(db.String(50), comment='SecretKey')
    disabled = db.Column(db.Boolean, nullable=False, default=False, comment='是否禁用')

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        self.disabled = True
        db.session.commit()
        return 'ok'


class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.String(16), default=objectid, primary_key=True, unique=True)
    name = db.Column(db.String(16), comment='数组名称')
    type = db.Column(db.Integer, comment='1:bool,2:int，3:str，')
    state = db.Column(db.Integer, comment='0:启用,1:禁用')
    note = db.Column(db.Text, comment='备注')


class Variable(db.Model):
    __tablename__ = 'variable'
    id = db.Column(db.Integer, nullable=False, default=1, autoincrement=True, primary_key=True, unique=True, comment='id')
    index = db.Column(db.Integer, autoincrement=True, default=1, unique=True, comment='数组索引')
    name = db.Column(db.String(50), comment='变量名')
    list_id = db.Column(db.String(16), db.ForeignKey('list.id'), comment='数组id')
    ratio = db.Column(db.Integer, default=1, comment='转换系数')
    note = db.Column(db.Text, comment='备注')
    state = db.Column(db.Boolean, comment='0:禁用，1:启用')
    disabled = db.Column(db.Boolean, nullable=False, default=False, comment='是否启用')

    def update(self):
        db.session.commit()
        return self

    def delete(self):
        self.disabled = True
        db.session.commit()
        return 'ok'


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, nullable=False, default=1, primary_key=True, autoincrement=True)
    name = db.Column(db.String(24), unique=True, nullable=False)
    desc = db.Column(db.Text)






