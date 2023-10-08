from flask import Blueprint, Response, flash, session, request, g, render_template, redirect, url_for, jsonify, make_response
from .forms import CreateUsuarioForm, LoginUsuarioForm, EventoForm, LugarForm
from .models import create_new_user, login_user, create_new_evento, create_new_lugar, get_lugares, get_eventos
import json

import datetime
from datetime import timedelta


agenda = Blueprint('agenda', __name__ , url_prefix = '/agenda')
home = Blueprint('home', __name__ )
usuario = Blueprint('usuario', __name__ , url_prefix = '/usuario')

@home.before_request
@agenda.before_request
def before_request():
    if "user" in session:

        g.user = session["user"]
    else:
        url_completa = request.url
        print("URL de la solicitud:", url_completa)
        g.user = None
        flash("Debe iniciar sesión para gestionar eventos", "error")
        return redirect(url_for('usuario.login'))
    

@usuario.before_request
def before():
    print(session)
    if "user" in session:
        g.user = session["user"]
    else:
        session.pop("user", None)
        #flash("Debe iniciar sesión para gestionar eventos ", "error")

@home.route("/")
def index():
    eventos = get_eventos()
    return render_template("inicio.html", eventos = eventos)

@usuario.route("/registro",  methods=["GET", 'POST'])
def registro():

    try:
        if not g.user and not session["user"]: 
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
        
        flash("Iniciaste sesión", "success")
        return redirect(url_for('home.index', user = g.user))
    except:
        return redirect(url_for('home.index', user = g.user))
        

    

@usuario.route("/login",  methods=["GET", 'POST'])
def login():
        login_form= LoginUsuarioForm()

        if request.method == 'POST' :
            email = login_form.email_usuario.data
            pwd = login_form.pwd_usuario.data
            
            #print ("estoy en login voy a buscar ",email,pwd)
            user = login_user(email, pwd)
            if user:
                #flash("Usuario encontrado!", 'success')
                session["user"] = [{"id":user.id, "n_usuario":user.n_usuario, "email_usuario":user.email_usuario}]
                return redirect(url_for('home.index', user = session["user"]))
            else:
                flash("No se encontro el usuario!", 'error')
  
        return render_template('login.html', form=login_form)

@usuario.route("/logout",  methods=["GET", 'POST'])
def logout():
    g.user=None
    session.pop("user", None)
    print("Se cerró sesión")
    return redirect(url_for('home.index',user=g.user))

@agenda.route("/admin", methods=["GET", "POST"])
def admin():
    form_lugar = LugarForm()
    lugares = obtener_lugares()
    if request.method == "POST":
        None
    return render_template('admin.html', form_lugar=form_lugar, lugares=lugares)


@agenda.route("/nuevo", methods=["GET", 'POST'])
def nuevo_evento():
    form_evento=EventoForm()

    if request.method == 'POST':
        n_evento = form_evento.n_evento.data
        d_evento = form_evento.d_evento.data
        #k_artista =  form_evento(form_new_release.k_artista.data)
        f_evento = form_evento.f_evento.data
        modalidad = form_evento.k_modalidad.data
        k_lugar = form_evento.k_lugar.data
        k_evento= create_new_evento(n_evento, d_evento, f_evento, modalidad, k_lugar, "CREADO", g.user[0]["id"])

        
        if k_evento:
            flash("Evento agregado!",  'success')
            return redirect(url_for('home.index'))

        else:
            flash("No se pudo registrar el evento", 'error')
            return redirect(url_for('home.index'))
        
    lugares = obtener_lugares()
    form_evento.k_lugar.choices = [(lugar.id, lugar.n_lugar) for lugar in lugares]
    print("global!!!!!->", g.user)
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
        eventos = get_lugares()
        
        json_eventos = []
        for e in eventos:
            #print(vars(e))
            json_eventos.append(e.to_dict())
        print(json_eventos)
        return json_eventos
    
@agenda.route("/",methods=["GET"] )
def mis_eventos():
    eventos = get_eventos(g.user[0]["id"])
    return render_template("inicio.html", eventos = eventos)

def obtener_lugares():
    lugares = get_lugares()
    return lugares

