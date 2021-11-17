from flask import Flask, render_template, jsonify
from flask.wrappers import Response
import random
from traccing import tracing
import time

app = Flask(__name__, template_folder='templates')

nomes = ['Miguel', 
        'Arthur', 
        'Heitor', 
        'Helena',
        'Alice',
        'Theo',
        'Davi',
        'Laura',
        'Gabriel',
        'Gael',
        'Bernardo',
        'Samuel',
        'Valentina',
        'João Miguel',
        'Enzo Gabriel',
        'Heloísa',
        'Pedro',
        'Lorenzo',
        'Sophia',
        'Maria Clara',
        'Maria Júlia',
        'Maria Eduarda',
        'Lorena',
        'Lucas',
        'Manuela',
        'Cecília',
        'Maria Cecília',
        'Benício',
        'Júlia',
        'Isabella']

sobrenomes = ['Silva', 
              'Santos', 
              'Oliveira', 
              'Souza',
              'Rodrigues', 
              'Ferreira', 
              'Alves', 
              'Pereira',
              'Lima', 
              'Gomes', 
              'Ribeiro', 
              'Martins']

@app.route('/nomecompleto', methods=['GET'])
@tracing.trace()
def index():
    index = random.randint(0, len(nomes))
    nome = nomes[index]
    index = random.randint(0, len(sobrenomes))
    sobrenome = sobrenomes[index] 
    nome_completo = nome + ' ' + sobrenome 
    time.sleep(float(random.randrange(0, 200))/100)
    return jsonify({'nomeCompleto': nome_completo})

if __name__ == '__main__':
    app.run()