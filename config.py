import os

class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_POOL_RECYCLE = 3600
    WTF_CSRF_ENABLED = True
    AWS_ACCESS_KEY = os.getenv('VAA3D_AWS_ACCESS_KEY', 'password')
    AWS_SECRET_KEY = os.getenv('VAA3D_AWS_SECRET_KEY', 'password')

class ProdConfig(Config):
    DB_DRIVER = 'mysql+pymysql://'
    DB_HOSTNAME = 'bigneuron.clwja7eltdnj.us-west-2.rds.amazonaws.com'
    DB_PORT = '3306'
    DB_NAME = 'vaa3d'
    DB_USERNAME = 'vaa3d'
    DB_PASSWORD = os.getenv('VAA3D_DB_PASSWORD', 'password')
    SQLALCHEMY_DATABASE_URI = DB_DRIVER + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOSTNAME + ':' + DB_PORT + '/' + DB_NAME
    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'secret_key')

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = 'secret'
    TESTING = True
