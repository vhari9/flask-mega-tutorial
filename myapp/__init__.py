from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.lastuser import LastUser
from flask_debugtoolbar import DebugToolbarExtension
import config

__all__ = ['app', 'db', 'manager', 'lastuser']

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
lastuser = LastUser()
lastuser.init_app(app)
toolbar = DebugToolbarExtension(app)

from myapp import views, models

