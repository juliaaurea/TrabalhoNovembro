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
        flash('Preecha todos os campos!')
        return redirect('/restaurantes/add')

@bp_restaurantes.route("/remove/<int:id>")
def remove(id_restaurantes):
    dados = Restaurantes.query.all(id_restaurantes)
    try:
        db.session.delete(dados)
        db.session.commit()
        flash("Restaurante removido!")
    except:
        flash("Restaurante inválido!")
    return redirect("/restaurantes")

@bp_restaurantes.route("/edit/<int:id>")
def edit(id):
    dados = Restaurantes.query.all(id_restaurantes)
    return render_template("restaurantes_editar.html", dados=dados)

@bp_restaurantes.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    localizacao = request.form.get("localizacao")
    id_restaurantes = request.form.get("id_restaurantes")
    
    if nome and localizacao and id_restaurantes:
        dados = Restaurantes.query.get(id_restaurantes)
        dados.nome = nome
        dados.localizacao = localizacao
        db.session.commit()
        flash("Restaurante editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/restaurantes")