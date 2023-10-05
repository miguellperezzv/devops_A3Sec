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

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.title[:10])




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