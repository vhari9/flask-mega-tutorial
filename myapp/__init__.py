# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.lastuser import LastUser
from flask.ext.lastuser.sqlalchemy import UserManager
from baseframe import baseframe, assets, Version
from flask_bootstrap import Bootstrap
import coaster.app
import config
from werkzeug.contrib.profiler import ProfilerMiddleware
import logging
import sys

__all__ = ['app', 'manager', 'lastuser', 'init_for', 'db']

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.DevelopmentConfig')
lastuser = LastUser()

from . import views, models
from .models import db

def init_for(env):
    if app.config['PROFILE']:
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

    if app.debug:
        # Turn off Werkzeug debug in console
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        # Enable our own logging for signals!
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    coaster.app.init_app(app, env)
    db.init_app(app)
    db.app = app
    baseframe.init_app(app, requires=['bootstrap', 'jquery', 'myapp'])
    lastuser.init_app(app)
    lastuser.init_usermanager(UserManager(db, models.User))
    Bootstrap(app)


