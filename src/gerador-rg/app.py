from flask import Flask, jsonify
from traccing import tracing
from random import randint, randrange
import time

app = Flask(__name__, template_folder='templates')

def gerador_rg():                                                        
    numeros = ''
    for n in range(8):
        numeros += str(randint(0, 9))

    soma_produtos = 0
    for i, n in enumerate(numeros):
        soma_produtos += int(n) * (i+2)

    if soma_produtos % 11 > 2:
        numeros += str(11 - (soma_produtos % 11))
    else:
        numeros += '0'

    return numeros

@app.route('/rg', methods=['GET'])
@tracing.trace()
def index():
    #time.sleep(float(randrange(0, 200))/100)
    return jsonify({'rg': gerador_rg()})

if __name__ == '__main__':
    app.run()