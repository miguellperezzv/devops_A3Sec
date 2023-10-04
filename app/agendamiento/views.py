from flask import Blueprint, Response, flash, session, request, g, render_template, redirect, url_for, jsonify, make_response



agenda = Blueprint('agenda', __name__ , url_prefix = '/agenda')
home = Blueprint('home', __name__ )
login = Blueprint('login', __name__ , url_prefix = '/agenda')

@agenda.route("/")
def index():
    return render_template("inicio.html")