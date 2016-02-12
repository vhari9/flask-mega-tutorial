# -*- coding: utf-8 -*-

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
    MAIL_PASSWORD = ''
    MAIL_SUPRESS_SEND = True

class DevelopmentConfig(Config,MailConfig):
    DEBUG = True
    SERVER_NAME = ''
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE = ''
    SQLALCHEMY_DATABASE_URI = '' + DATABASE
    SECRET_KEY = ''
    CACHE_TYPE = 'simple'