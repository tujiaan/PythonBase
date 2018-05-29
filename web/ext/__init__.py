# from .uploads import uploads

from .babel import babel
from .cache import cache
from .cors import cors
from .csrf import csrf
from .db import db
from .redis import redis


def ext_init(app):
    db.init_app(app)
    cache.init_app(app)
    csrf.init_app(app)
    babel.init_app(app)
    redis.init_app(app)
    cors.init_app(app)
