from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario/insert', methods=['POST'])
def usuario_inserir():
    data = None #funcao do luiz para inserir
    if data:
        flash(f'usuario {data.nome}, criado com sucesso!')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
