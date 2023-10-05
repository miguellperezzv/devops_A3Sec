from flask import Blueprint, Response, flash, session, request, g, render_template, redirect, url_for, jsonify, make_response
from .forms import CreateUsuarioForm, LoginUsuarioForm
from .models import create_new_user, login_user

import datetime
from datetime import timedelta


agenda = Blueprint('agenda', __name__ , url_prefix = '/agenda')
home = Blueprint('home', __name__ )
usuario = Blueprint('usuario', __name__ , url_prefix = '/usuario')

@home.before_request
@usuario.before_request
@agenda.before_request
def before_request():
    if "user" in session:
        g.user = session["user"]
    else:
        g.user = None

    
    g.datetime = datetime.datetime
    print("DATETIME "+ str(g.datetime.now()))



@home.route("/")
def index():
    return render_template("inicio.html")

@usuario.route("/registro",  methods=["GET", 'POST'])
def registro():

    if not g.user: 
        form_signup= CreateUsuarioForm()

        if request.method == 'POST' :
            name = form_signup.name.data
            email = form_signup.email_usuario.data
            pwd = form_signup.pwd_usuario.data
            
            result = create_new_user(name, email, pwd)
            if result:
                flash("Usuario creado!")
            else:
                flash("No se creo el Usuario!")
            return redirect(url_for('home.index',user=g.user))
        return render_template('registro.html', form=form_signup)
    
    flash("You're already logged in.", "alert-primary")
    return redirect(url_for('home.index', user = g.user))

@usuario.route("/login",  methods=["GET", 'POST'])
def login():

    if not g.user: 
        login_form= LoginUsuarioForm()

        if request.method == 'POST' :
            email = login_form.email_usuario.data
            pwd = login_form.pwd_usuario.data
            
            #print ("estoy en login voy a buscar ",email,pwd)
            user = login_user(email, pwd)
            if user:
                #flash("Usuario encontrado!", 'success')
                return redirect(url_for('home.index',user=g.user))
            else:
                flash("No se encontro el usuario!", 'error')
            
        return render_template('login.html', form=login_form)
    
    flash("You're already logged in.", "alert-primary")
    

