from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from ..db import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer(), primary_key=True)
    n_usuario = db.Column(db.String(40), nullable = False)
    email_usuario = db.Column(db.String(50), nullable = False)
    pwd_usuario = db.Column(db.String(200), nullable = False)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)   

    # FK 
    #eventos_creados = db.relationship('Evento', backref='creador')  

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.n_usuario)
    
class Evento(db.Model):
    __tablename__ = 'Evento'
    id = db.Column(db.Integer(), primary_key=True)
    n_evento = db.Column(db.String(40), nullable = False)
    d_evento = db.Column(db.String(200), nullable = True)
    f_evento = db.Column(db.DateTime(), default=datetime.utcnow, nullable = False)
    modalidad = db.Column(db.String(40), nullable = False)
    estado = db.Column(db.String(20), nullable = False)

    # NORMALIZACION
    k_usuario = db.Column(db.Integer(), db.ForeignKey('Usuario.id'))
    k_lugar = db.Column(db.Integer(), db.ForeignKey('Lugar.id'))

    # FK's
    #creador = db.relationship("Usuario", back_populates="eventos_creados")  # Cambiar 'usuario_eventos' a 'eventos_creados'
    #ubicacion = db.relationship("Lugar", back_populates="lugar_eventos")

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.n_evento)
    
class Lugar(db.Model):
    __tablename__ = 'Lugar'
    id = db.Column(db.Integer(), primary_key=True)
    n_lugar = db.Column(db.String(40), nullable = False)
    d_lugar = db.Column(db.String(200), nullable = True)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    

    lugar_eventos = db.relationship('Evento', backref='ubicacion') 

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.n_lugar)

#####################################Funciones 
#mis consultas 
def create_new_user(n_usuario, email, password):
    print(email)
    print(password)

    #k_usuario = "U"+str(len(get_all_users())+1)
    user = Usuario( n_usuario =n_usuario, email_usuario=email, pwd_usuario=password )
    
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        print ("No se registró el usuario "+ str(e))
        return None

def login_user(email, password):
    
    user_found = db.session.query(Usuario).filter_by(email_usuario=email, pwd_usuario = password).first()
    if user_found:
        return user_found
    else:
        print("No se encontró el usuario ")
        return None
    
def create_new_evento (n_evento, d_evento, f_evento, modalidad, estado, k_lugar, k_usuario):
    None
    evento = Evento(  n_evento = n_evento, d_evento = d_evento, f_evento = f_evento, modalidad = modalidad, estado=estado, k_lugar = k_lugar, k_usuario  = k_usuario )

    try:
        db.session.add(evento)
        db.session.commit()
        return evento
    except Exception as e:
        print ("No se registró el evento "+ str(e))
        return None    
    
def create_new_lugar(n_lugar,d_lugar):
    lugar = Lugar(n_lugar = n_lugar,d_lugar=d_lugar)
    try:
        db.session.add(lugar)
        db.session.commit()
        return lugar.id
    except Exception as e:
        print ("No se registró el evento "+ str(e))
        return None     
    
def get_eventos():
    eventos = db.session.query(Evento).all()
    return eventos