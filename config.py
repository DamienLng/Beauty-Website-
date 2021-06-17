import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thiskeyistopsecretonlyIshouldknow'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///Beauty.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO shows SQL commands used to exceute a query
    SQLALCHEMY_ECHO = False
    DEBUG = True