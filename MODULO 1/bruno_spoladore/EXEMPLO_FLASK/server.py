import json
from datetime import date
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def server():
    return 'Hello Flask'


@app.route('/saudacoes')
def method_name():
    return 'Boa tarde, amigo'


@app.route('/amigos-json')
def my_friends_to_json():
    return json.dumps(["jao", "zezin", "pedrin"])


@app.route('/diga-data/<string:dma>')
def data(dma):
    mens = "não entendi"
    if dma == 'dia':
        mens = date.today().day
    elif dma == 'mes':
        mens = date.today().month
    elif dma == 'ano':
        mens = date.today().year
    return str(mens)


@app.route('/diga-data/<string:dma>/<string:formato>')
def data_formato(dma, formato):
    mens = "não entendi"
    if dma == 'dia':
        mens = date.today().day
    elif dma == 'mes':
        mens = date.today().month
    elif dma == 'ano':
        mens = date.today().year
    if formato == 'xml':
        mens = f"<{dma}>{mens}</{dma}>"
    elif formato == 'json':
        mens = f'''{{"{dma}":{mens}}}'''
    print(mens)
    return str(mens)


@app.route('/data-query')
def data_query():
    params = request.args
    print(params)  # ImmutableMultiDict([('nome', 'silvio')])
    print(params['nome'])  # silvio
    print(params['cargo'])  # professor
    print(json.dumps(params))  # {"nome": "silvio", "cargo": "professor"}
    return "Olá " + params['nome']


if __name__ == "__main__":
    app.run(debug=True)
