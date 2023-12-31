import os
from os import environ
import datetime

UPLOAD_FOLDER = os.path.abspath("./uploads/")
DB_URI = "TBD"

class Config(object):
    DEBUG = True
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    # OJO: PARA CUANDO TRABAJE EN MEMORIA   SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:" 
    #SQLALCHEMY_DATABASE_URI = "sqlite:///musicalbox.sqlite3"
    #SQLALCHEMY_DATABASE_URI = "sqlite:///TES.sqlite3"
    #SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER
    
    

class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY", 123456)
    SQLALCHEMY_DATABASE_URI = DB_URI
        #FLASK_DEBUG = True
    FLASK_ENV='development'
    DEBUG=True
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    PWD = os.path.abspath(os.curdir)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URL')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=180)

class DevelopmentConfig(Config):
    #FLASK_DEBUG = True
    FLASK_ENV='development'
    DEBUG=True
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    PWD = os.path.abspath(os.curdir)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/agendamiento.sqlite'.format(PWD)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = environ.get('DB_URL')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=180)