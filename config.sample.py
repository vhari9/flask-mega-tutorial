# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    pass

class MailConfig():
    # Use SMTP settings for your email provider
    MAIL_SERVER = ''
    MAIL_PORT = ''
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = '' # If you have 2FA enabled, then use app-specific password
    MAIL_SUPRESS_SEND = True # Email is never sent, gets logged to console

class DevelopmentConfig(Config,MailConfig):
    DEBUG = True
    SERVER_NAME = ''
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE = os.path.join(basedir, '')
    SQLALCHEMY_DATABASE_URI = '' + DATABASE
    SECRET_KEY = ''
    CACHE_TYPE = 'simple'