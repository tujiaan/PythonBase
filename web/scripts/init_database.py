from web.models import *


def init():
    try:
        db.drop_all()
        pass
    except:
        pass
    db.create_all()
