from flask import Flask, render_template, url_for, request, flash, redirect
from bd import *
app = Flask(__name__)
app.secret_key = """Kazakhstan greatest country in the world
All other countries are run by little girls
Kazakhstan number one exporter of potassium"""

usuario_logado = None
@app.route('/')
def index():
    global  usuario_logado
    usuario_logado = None
    return render_template('login.html', flag=False)

@app.route('/inicio')
def inicio():
    dados = {}
    dados['url_form'] = url_for('redireciona_criar_carona')
    dados['url_buscar'] = url_for('redireciona_busca_carona')
    ofertadas = buscar_rota_oferecida(usuario_logado.id)
    inscrita = buscar_rota_inscrita(usuario_logado.id)
    return render_template('index.html', dados=dados, ofertadas=ofertadas, inscrita=inscrita, flag=True)

@app.route('/logar')
def logar():
    return render_template('login.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html', flag=False)

@app.route('/criar/rota')
def chama_criar_rota():
    return render_template('criar_carona.html', flag=True)


@app.route('/buscar/rota')
def chama_buscar_rota():
    return render_template('buscar_carona.html', flag=True)

@app.route('/redireciona_criar_carona', methods=['POST'])
def redireciona_criar_carona():
    dados = {}
    dados['url_form'] = url_for('rota_inserir')
    return render_template('criar_carona.html', flag=True)

@app.route('/rota_inserir', methods=['POST'])
def rota_inserir():
    dados = {}
    dados['url_form'] = url_for('redireciona_criar_carona')
    data = adicionar_rota(request, usuario_logado.id)
    return redirect('/inicio')

@app.route('/redireciona_busca_carona', methods=['POST'])
def redireciona_busca_carona():
    dados = {}
    dados['url_form'] = url_for('rota_inserir')
    return render_template('buscar_carona.html', flag=True)

@app.route('/buscar_carona', methods=['POST'])
def rota_buscar():
    data = buscar_carona(request)
    return render_template('buscar_carona.html', resultado=data, flag=True)


@app.route('/confirmar_inscricao/<int:id>')
def salvar_inscricao(id):
    id = int(id)
    data = salvar_inscricao_rota(id, usuario_logado.id)
    return redirect(url_for('inicio'))


@app.route('/usuario_inserir', methods=['POST'])
def usuario_inserir():
    dados = {}
    dados['url_form'] = url_for('usuario_inserir')
    data = adicionar_usuario(request)
    return redirect('/logar')

@app.route('/login', methods=['POST'])
def usuario_login():
    global  usuario_logado
    usuario_logado = verificar_login(request)
    dados = {}
    if usuario_logado:
        dados = {}
        dados['url_form'] = url_for('usuario_login')
        dados['url_form'] = url_for('usuario_inserir')
        return redirect('/inicio')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
