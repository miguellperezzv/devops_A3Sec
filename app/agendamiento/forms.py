from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SelectField, PasswordField, IntegerField, FileField, DateTimeField, DateField
from wtforms.fields import DateTimeLocalField
#from wtforms.fields.html5 import DateField
from datetime import date, datetime
#from wtforms.ext.sqlalchemy.fields import QuerySelectField
#from wtforms.widgets import html5 as h5widgets
#import pycountry



class CreateUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Nombre")])
    #lastname = StringField('Apellido', validators= [DataRequired(message = "Ingresa un apellido")])
    email_usuario = StringField('Email', validators=[DataRequired(message = "Ingrese un e-mail")])
    pwd_usuario = PasswordField('Contraseña', validators=[DataRequired(message="Ingrese una contraseña.")])

class LoginUsuarioForm(FlaskForm):
    email_usuario =  StringField('Email', validators=[DataRequired()])
    pwd_usuario =  PasswordField('Contraseña', validators=[DataRequired()])

class EditUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Ingresa un nombre")])
    lastname = StringField('Apellido', validators= [DataRequired(message = "Ingresa un apellido")])
    email_usuario = StringField('Email', validators=[DataRequired(message = "Ingresa un e-mail válido")])
    pwd_usuario = PasswordField('Contraseña', validators=[DataRequired(message="Ingresa una contraseña.")])
    address = StringField('Dirección', validators=[DataRequired(message="Dirección a donde te enviaremos tus productos")])
    city = StringField('Municipio/Ciudad', id="city", validators=[DataRequired(message="Lugar a donde te enviaremos tus productos")])

class EventoForm(FlaskForm):
    n_evento = StringField('Nombre', validators=[DataRequired(message="Nombre del evento")])
    d_evento = StringField('Descripción', validators=[DataRequired(message="Descricpión del evento")])
    #f_evento = DateField("Fecha de Lanzamiento", default=date.today, format='%Y-%m-%d %H:%M')
    f_evento = DateTimeLocalField("Fecha de Lanzamiento", default=date.today, format='%Y-%m-%d %H:%M')
    k_modalidad = SelectField("Modalidad", id="modalidad", choices=["PRESENCIAL", "VIRTUAL"])
    k_lugar = SelectField('Selecciona un lugar', coerce=int)
    
    #lugares = obtener_lugares()

    #k_lugar = SelectField("Lugar", id="lugar", choices=[ (lugar.id, lugar.n_lugar) for lugar in lugares])

class LugarForm(FlaskForm):
    n_lugar = StringField('Lugar', validators=[DataRequired(message="Nombre del lugar")])
    d_lugar = StringField('Descripcion', validators=[DataRequired(message="Descripción del lugar")])


    

    