from flask import Blueprint, Response, flash, session, request, g, render_template, redirect, url_for, jsonify, make_response
from .forms import CreateUsuarioForm, LoginUsuarioForm, EventoForm
from .models import create_new_user, login_user, create_new_evento, create_new_lugar, get_eventos

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
    
    flash("You're already logged in.", "success")

@agenda.route("/nuevo", methods=["GET", 'POST'])
def nuevo_evento():
    form_evento=EventoForm()

    if request.method == 'POST':
        n_evento = form_evento.name.data
        d_evento = form_evento.descr.data
        #k_artista =  form_evento(form_new_release.k_artista.data)
        f_evento = form_evento.fecha.data
        modalidad = form_evento.k_modalidad.data

        k_evento= create_new_evento(n_evento, d_evento, f_evento, modalidad)
        
        if k_evento:
            flash("Evento agregado!")
            return redirect(url_for('home.index'), 'success')

        else:
            flash("No se pudo registrar el evento", 'error')
            return redirect(url_for('home.index'))
    return render_template("nuevo_evento.html", form = form_evento )


@agenda.route("/lugar", methods=["GET", 'POST'])
def nuevo_lugar():
    if request.method == 'POST':
        data = request.json
        n_lugar = data["n_lugar"]
        d_lugar = data["d_lugar"]
        print("RESPONSE "+n_lugar)
        k_evento = create_new_lugar(n_lugar,d_lugar)

        if k_evento:
            return {"message":"Lugar "+str(k_evento)+"creado! "},200
        else:
            return {"message":"No se pudo crear el Lugar! "},400
    elif request.method == 'GET':
        eventos = get_eventos()
        return eventos

