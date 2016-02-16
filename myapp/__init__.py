# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.lastuser import LastUser
from flask.ext.lastuser.sqlalchemy import UserManager
from baseframe import baseframe, assets, Version
from flask_bootstrap import Bootstrap
# from flask_debugtoolbar import DebugToolbarExtension
import coaster.app
import config

__all__ = ['app', 'manager', 'lastuser', 'init_for', 'db']

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.DevelopmentConfig')
lastuser = LastUser()

from . import views, models
from .models import db

def init_for(env):
    coaster.app.init_app(app, env)
    db.init_app(app)
    db.app = app
    baseframe.init_app(app, requires=['myapp'])
    lastuser.init_app(app)
    lastuser.init_usermanager(UserManager(db, models.User))
    Bootstrap(app)
    # toolbar = DebugToolbarExtension(app)
