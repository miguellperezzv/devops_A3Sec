from .config import DevelopmentConfig
from flask import Flask, jsonify, g
from .db import db
from .agendamiento.views import home, agenda, usuario
from .agendamiento.models import    Usuario
from os import environ
from flask_jwt_extended import JWTManager
import datetime




ENDPOINTS = [('/',home),('/agenda',agenda), ('/usuario', usuario) ]

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    #app.config.from_envvar('CONFIG_SETTINGS')

    db.init_app(app)
    #ma.init_app(app)
    app.config["JWT_SECRET_KEY"] = "holaMundo" 
    jwt = JWTManager(app)
    app.config['SECRET_KEY'] = 'holaMundo'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'
    
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=10)

    with app.app_context():
        db.create_all()
        #usuario = Usuario(usuario="admin",password = "contrasenha")	
        #db.session.add_all([usuario])
        #db.session.commit()







    # register each active blueprint
    for url, blueprint in ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app



