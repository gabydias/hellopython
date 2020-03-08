# Importando o módulo do Flask e o módulo os
from flask import Flask, render_template
from redis import Redis, RedisError
import pymysql

import os

# Connect to Redis
redis = Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)

# Objeto da Classe Flask que vamos usar para configurar e executar a aplicação
app = Flask(__name__)

# Conexão Simples com o MySQL
class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "appuser"
        password = "213"
        db = "sre_stack"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_db(self):
        self.cur.execute("SELECT * FROM tecnologias")
        result = self.cur.fetchall()
        return result

# Definindo a rota padrão da aplicação.
@app.route("/")

# Função que tem como objetivo printar uma mensagem já em formato HTML na tela.
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "cannot connect to Redis, counter disabled"

    def db_query():
        db = Database()
        techs = db.list_db()
        return techs
    res = db_query()

    return render_template('index.html', visits=visits, result=res)

# Garantindo que o módulo não será executado se ele for importado por outro módulo.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
