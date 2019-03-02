import os


class Config(object):
    SECRET_KEY = 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://raferti:1@localhost/test2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
