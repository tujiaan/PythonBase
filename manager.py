from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from web import create_app
from web.ext import db
from instance.config import SQLALCHEMY_DATABASE_URI
from web.models import *

app = create_app()
app.config[SQLALCHEMY_DATABASE_URI] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/firefighting'
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run( )