from flask import Flask, render_template
from flask.wrappers import Response
from traccing import tracing, opentracing_tracer
import opentracing
import requests
import logging
import os

app = Flask(__name__, template_folder='templates')

URL_GERADOR_NOME = os.getenv("URL_GERADOR_NOME", "gerador-nome:5000")
URL_GERADOR_DOCUMENTO = os.getenv("URL_GERADOR_DOCUMENTO", "gerador-documento:5000")

@app.route('/', methods=['GET'])
@tracing.trace()
def index():    

    span = tracing.get_span()
    
    text_carrier = {}
    opentracing_tracer.inject(span, opentracing.Format.TEXT_MAP, text_carrier)
    response_nome = requests.get('http://' + URL_GERADOR_NOME + '/nomecompleto', headers=text_carrier)
    nome = response_nome.json()

    response_documento = requests.get('http://' + URL_GERADOR_DOCUMENTO + '/documento', headers=text_carrier)
    documento = response_documento.json()

    # Log para incluir o evento no Jaeger
    span.log_kv({'event': 'Carregando os dados da pessoa.'})

    logging.warning('Carregando os dados da pessoa.')

    pessoa = {'nome': nome['nomeCompleto'], 'cpf': documento['cpf'], 'rg': documento['rg']}

    return render_template('index.html', pessoa=pessoa)

if __name__ == '__main__':
    app.run()