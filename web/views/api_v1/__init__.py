import flask_restplus
from .student import api as s_ns
from.user import api as user_ns
from .topic import api as topic_ns

api = flask_restplus.Api(
    title="长行物流API",
    description="长行物流货主端API",
    contact="宁夏巫迪科技有限公司",
    contact_url="https://woody.technology",
    contact_email="kaive@woody.vip",
    version="1.0")

api.add_namespace(s_ns, path='/student')
api.add_namespace(user_ns, path='/user')
api.add_namespace(topic_ns, path='/topic')
