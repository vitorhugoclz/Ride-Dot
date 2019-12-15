from flask import Flask, render_template, url_for, request, flash, redirect
from bd import *
app = Flask(__name__)
app.secret_key = """Kazakhstan greatest country in the world
All other countries are run by little girls
Kazakhstan number one exporter of potassium"""

usuario_logado = None
@app.route('/')
def index():
    dados = {}
    dados['url_form'] = url_for('redireciona_criar_carona')
    return render_template('index.html', dados=dados)

##funcoes abaixo ainda nao integradas como nova pagina 
@app.route('/redireciona_criar_carona', methods=['POST'])
def redireciona_criar_carona():
    dados = {}
    dados['url_form'] = url_for('rota_inserir')
    return render_template('criar_carona.html')
@app.route('/rota_inserir', methods=['POST'])
def rota_inserir():
    dados = {}
    dados['url_form'] = url_for('redireciona_criar_carona')
    data = adicionar_rota(request)
    return render_template('index.html', dados=dados)

'''@app.route('/usuario/inserir', methods=['POST'])
def usuario_inserir():
    dados = {}
    dados['url_form'] = url_for('usuario_inserir')
    data = adicionar_usuario(request)
    if data:
        flash(f'Usuario: {data.nome} criado com sucesso')
    return render_template('usuario_form.html', dados=dados)

@app.route('/login', methods=['POST'])
def usuario_login():
    usuario_logado = verificar_login(request)
    dados = {}
    if usuario_logado:
        dados = {}
        dados['url_form'] = url_for('usuario_login')
        print("logou")
        dados['url_form'] = url_for('usuario_inserir')
        return render_template('usuario_form.html', dados=dados)
    else:
        print("nao logou")
        return render_template('usuario_form.html', dados=dados)'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
