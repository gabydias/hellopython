# Importando o módulo do Flask e o módulo os
from flask import Flask, render_template

import os

# Objeto da Classe Flask que vamos usar para configurar e executar a aplicação
app = Flask(__name__)

# Definindo a rota padrão da aplicação.
@app.route("/")

# Função que tem como objetivo renderizar uma página html.
def hello():

    return render_template('index.html')

# Garantindo que o módulo não será executado se ele for importado por outro módulo.
if __name__ == "__main__":
    app.run(host='0.0.0.0')
