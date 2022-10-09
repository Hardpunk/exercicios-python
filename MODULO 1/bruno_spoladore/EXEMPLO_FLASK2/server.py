from flask import Flask, render_template

app = Flask(__name__)
titulo = "Estamos aprendendo Flask"


@app.route('/')
def hello():
    return render_template('index.html', titulo=titulo)


def f():
    global titulo
    titulo = "Oi"

if __name__ == '__main__':
    app.run()
