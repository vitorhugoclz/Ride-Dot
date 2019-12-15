from flask import Flask, render_template, url_for, request, flash, redirect
from bd import *
app = Flask(__name__)


@app.route('/')
def index():
    dados = {}
    dados['url_form'] = url_for('usuario_inserir')
    return render_template('usuario_form.html', dados=dados)

@app.route('/usuario/inserir', methods=['POST'])
def usuario_inserir():
    dados = {}
    dados['url_form'] = url_for('usuario_inserir')
    adicionar_usuario(request)
    return render_template('usuario_form.html', dados=dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
