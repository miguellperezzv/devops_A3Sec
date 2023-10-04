from .config import DevelopmentConfig
from flask import Flask, jsonify, g
#from db import db, ma 
from .agendamiento.views import home, agenda, login



ENDPOINTS = [('/',home),('/agenda',agenda), ('/login', login) ]

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    #app.config.from_envvar('CONFIG_SETTINGS')

    #db.init_app(app)
    #ma.init_app(app)


    #with app.app_context():
    #    db.create_all()

    # register each active blueprint
    for url, blueprint in ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app



