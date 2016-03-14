import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_USER = os.environ['DATABASE_USER']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
