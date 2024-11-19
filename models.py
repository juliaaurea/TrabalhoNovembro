from database import db

class Restaurantes(db.Model):
    __tablename__ = 'restaurantes'
    id_restaurante = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    localizacao = db.Column(db.String(100))

    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao

    def __repr__(self):
        return "<Restaurante {}>".format(self.nome)

    
class Pratos(db.Model):
    __tablename__ = 'pratos'
    id_pratos = db.Column(db.Integer, primary_key=True)
    id_restaurantes = db.Column(db.Integer, db.ForeignKey('restaurantes.id'))
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float(10,2))

    restaurantes = db.relationship('Restaurantes', foreign_keys=id_restaurantes)

    def __init__(self, id_pratos, id_restaurantes, nome, preco):
        self.id_pratos = id_pratos
        self.id_restaurantes = id_restaurantes
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return "<Pratos {} - {} - {}>".format(self.restaurantes.nome, self.nome, self.preco)