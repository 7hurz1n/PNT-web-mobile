from threading import local

from flask import Blueprint,render_template, request

from db import db
from models import Ocorrencia
routes = Blueprint('app', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        ocorrencia = request.form['ocorrenciaForm']
        detalhes = request.form['detalhesForm']
        gravidade = request.form['gravidadeForm']
        local = request.form['localForm']
        data = request.form['dataForm']
        hora = request.form['horaForm']

        nova_ocorrencia = Ocorrencia(ocorrencia=ocorrencia, detalhes=detalhes, gravidade=gravidade, local=local, data=data, hora=hora)
        db.session.add(nova_ocorrencia)
        db.session.commit()

        return render_template('confirmacao.html', ocorrencia=ocorrencia, detalhes=detalhes, gravidade=gravidade, local=local, data=data, hora=hora)

@routes.route('/historico')
def historico():
    ocorrencias = Ocorrencia.query.all()
    return render_template('historico.html', ocorrencias=ocorrencias)

@routes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    ocorrencia = Ocorrencia.query.get(id)
    if request.method == 'GET':
        return render_template('editar.html', ocorrencia=ocorrencia)
    elif request.method == 'POST':
        ocorrencia.ocorrencia = request.form['ocorrenciaForm']
        ocorrencia.detalhes = request.form['detalhesForm']
        ocorrencia.gravidade = request.form['gravidadeForm']
        ocorrencia.local = request.form['localForm']
        ocorrencia.data = request.form['dataForm']
        ocorrencia.hora = request.form['horaForm']

        db.session.commit()

        return render_template('confirmacao.html', ocorrencia=ocorrencia.ocorrencia, detalhes=ocorrencia.detalhes, local=ocorrencia.local, data=ocorrencia.data, hora=ocorrencia.hora, gravidade=ocorrencia.gravidade)

@routes.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar(id):
    ocorrencia = Ocorrencia.query.get(id)
    db.session.delete(ocorrencia)
    db.session.commit()
    return render_template('deletado.html', ocorrencia=ocorrencia.ocorrencia, detalhes=ocorrencia.detalhes, local=ocorrencia.local, data=ocorrencia.data, hora=ocorrencia.hora, gravidade=ocorrencia.gravidade)
