import os
from flask import Flask, jsonify
from flask.wrappers import Response
from traccing import tracing, opentracing_tracer
import opentracing
import requests
import time

app = Flask(__name__)

URL_GERADOR_CPF = os.getenv("URL_GERADOR_CPF", "gerador-cpf:5000")
URL_GERADOR_RG = os.getenv("URL_GERADOR_RG", "gerador-rg:5000")

@app.route('/documento', methods=['GET'])
@tracing.trace()
def index():    

    span = tracing.get_span()
    text_carrier = {}
    opentracing_tracer.inject(span, opentracing.Format.TEXT_MAP, text_carrier)

    span.log_kv({'event': 'Carregando os dados de CPF.'})
    response_cpf = requests.get('http://' + URL_GERADOR_CPF + '/cpf', headers=text_carrier)
    cpf = response_cpf.json()

    span.log_kv({'event': 'Carregando os dados de RG.'})
    response_rg = requests.get('http://' + URL_GERADOR_RG + '/rg', headers=text_carrier)
    rg = response_rg.json()

    return jsonify({'cpf': cpf['cpf'], 'rg': rg['rg']})

if __name__ == '__main__':
    app.run()