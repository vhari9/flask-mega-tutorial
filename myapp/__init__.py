from flask.ext.lastuser import LastUser
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config

__all__ = ['app', 'db', 'manager']

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
lastuser = LastUser()
lastuser.init_app(app)

from myapp import views, models

