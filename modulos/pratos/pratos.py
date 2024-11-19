from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Restaurantes, Pratos

bp_pratos = Blueprint('pratos', __name__, template_folder="templates")

@bp_pratos.route('/')
def index():
    p = Pratos.query.all()
    return render_template('pratos.html', pratos=p)

@bp_pratos.route('/add')
def add():
    restaurantes = Restaurantes.query.all()
    p = Pratos.query.all()
    return render_template('pratos_add.html', restaurantes=restaurante, pratos=p)

@bp_pratos.route('/save', methods=['POST'])
def save():
    id_pratos = request.form.get('id_pratos')
    id_restaurantes = request.form.get('id_restaurantes')
    nome = request.form.get('nome')
    preco = request.form.get('preco')

    if id_pratos and id_restaurantes and nome and preco:
        objeto = Pratos(id_pratos, id_restaurantes , nome, preco)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido salvo com sucesso!')
        return redirect('/pratos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/pratos/add')