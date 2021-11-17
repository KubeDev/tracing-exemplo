from flask import Flask, render_template, jsonify
from flask.wrappers import Response
import random
from traccing import tracing
import time

app = Flask(__name__, template_folder='templates')

def gerador_cpf():                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                
        cpf.append(11 - val if val > 1 else 0)                                  
                                                                                
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

@app.route('/cpf', methods=['GET'])
@tracing.trace()
def index():
    #time.sleep(float(random.randrange(0, 200))/100)
    return jsonify({'cpf': gerador_cpf()})

if __name__ == '__main__':
    app.run()