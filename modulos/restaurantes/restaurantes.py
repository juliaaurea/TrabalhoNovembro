from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Restaurantes

bp_restaurantes = Blueprint('restaurantes', __name__, template_folder="templates")

@bp_restaurantes.route('/')
def index():
    dados = Restaurantes.query.all()
    return render_template('restaurantes.html', dados=dados)

@bp_restaurantes.route('/add')
def add():
    return render_template('restaurantes_add.html')

@bp_restaurantes.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    localizacao = request.form.get('localizacao')
    if nome and localizacao:
        objeto = Restaurantes(nome, localizacao)
        db.session.add(objeto)
        db.session.commit()
        flash('Restaurante cadastrado com sucesso!')
        return redirect('/restaurantes')
    else:
        flash('Restaurante todos os campos!')
        return redirect('/restaurantes/add')