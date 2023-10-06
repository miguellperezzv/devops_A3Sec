from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SelectField, PasswordField, IntegerField, FileField, DateTimeField
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
    f_evento = DateTimeField('Fecha del evento', validators=[DataRequired(message="Ingresa una fecha y hora especifica")])
    k_modalidad = SelectField("Modalidad", id="modalidad", choices=[])

    def __init__(self, modalidad: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if modalidad:
            self.k_modalidad.choices = ["PRESENCIAL", "VIRTUAL"]
    

    