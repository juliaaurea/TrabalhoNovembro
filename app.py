from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = "QualquerCoisaSecreta"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/restaurantes"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Restaurantes, Pratos

from modulos.restaurantes.restaurantes import bp_restaurantes
app.register_blueprint(bp_restaurantes, url_prefix='/restaurantes')

from modulos.pratos.pratos import bp_pratos
app.register_blueprint(bp_pratos, url_prefix='/pratos')

@app.route('/')
def index():
    return render_template('ola.html')


#Restaurantes: id_restaurante (INT, PRIMARY KEY), nome (VARCHAR(100)), localizacao (VARCHAR(100))
#Pratos: id_prato (INT, PRIMARY KEY), nome (VARCHAR(100)), preco (DECIMAL(10, 2)), id_restaurante (INT, FK)
#Relacionamento: 1 Restaurante 1 Pratos