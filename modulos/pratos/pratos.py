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
    p = Pratos.query.all()
    return render_template('pratos_add.html', pratos=p)

@bp_pratos.route('/save', methods=['POST'])
def save():
    id_pratos = request.form.get('id_pratos')
    nome = request.form.get('nome')
    preco = request.form.get('preco')

    if id_pratos and nome and preco:
        objeto = Pratos(id_pratos, nome, preco)
        db.session.add(objeto)
        db.session.commit()
        flash('Prato salvo com sucesso!')
        return redirect('/pratos')
    else:
        flash('Preencha todos os campos!')
        return redirect('/pratos/add')

@bp_pratos.route("/remove/<int:id>")
def remove(id_pratos):
    p = Pratos.query.get(id_pratos)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Prato removido!")
    except:
        flash("Prato inválido!")
    return redirect("/pratos")

@bp_pratos.route("/edit/<int:id>")
def edit(id_pratos):
    p = Pratos.query.get(id_pratos)
    r = Restaurantes.query.all()
    return render_template("pratos_editar.html", pratos=p, restaurantes=r)

@bp_pratos.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    preco = request.form.get("preco")
    id_restaurantes = request.form.get("id_restaurantes")
    id_pratos = request.form.get("id_pratos")
    
    if nome and preco and id_pratos and id_restaurantes:
        p = Pratos.query.get(id_pratos)
        p.nome = nome
        p.preco = preco
        p.id_restaurantes = id_restaurantes
        db.session.commit()
        flash("Prato editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/pratos")