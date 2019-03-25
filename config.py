import os


class Config(object):
    SECRET_KEY = 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://raferti:1@localhost/test2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['raferti712@yandex.ru']

    POSTS_PER_PAGE = 3