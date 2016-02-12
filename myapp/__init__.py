from flask import Flask, _app_ctx_stack
from flask.ext.sqlalchemy import SQLAlchemy
import config

__all__ = ['app', 'db', 'manager']

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from myapp import views, models

