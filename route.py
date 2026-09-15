from flask import Blueprint,render_template, request

from db import db
from models import Ocorrencia
routes = Blueprint('app', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        email = request.form['emailForm']
        senha = request.form['senhaForm']

        novo_usuario = Ocorrencia(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        return render_template('user.html', nome=nome, email=email)
