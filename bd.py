import os
import populate_db
from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, DateTimeField, DateField, \
    DecimalField, FloatField

database = SqliteDatabase('ride_dote.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class ModelBase(Model):  # classe modelo
    """
       Classe que cria a Entidade modelo a ser usada no projeto através da biblioteca peewee.
       Best practice: define a base model class that points at the database object you wish to use,
       and then all your models will extend it:
    """
    class Meta:
        """
           Meta classe que ao ser herdada define o metodo de conexao atravez do objeto database
        """
        database = database


class Usuario(ModelBase):

    """Classe para persistencia de um usuario genérico"""
    nome = CharField()
    email = CharField(unique=True)
    nome_usuario = CharField(unique=True)
    foto = CharField(null=True, default=None)
    senha = CharField()
    cpf = CharField(unique=True)
    numero_telefone = CharField(null=True)
    media_avaliacao = FloatField(default=0.0)


class Avaliacao(ModelBase):
    nota = FloatField()
    comentario = CharField(null=True, default=None)
    data = DateField()
    usuario_id = ForeignKeyField(Usuario)


class Rota(ModelBase):
    cidade_origem = CharField()
    cidade_destino = CharField()
    usuario_ofertante = ForeignKeyField(Usuario)

class CidadesIntermediarias(ModelBase):
    cidade = CharField()
    rota_id = ForeignKeyField(Rota)


def create_tables():
    """cria as tabelas do banco de dados"""
    database.connect()
    database.create_tables([Usuario, Avaliacao, Rota, CidadesIntermediarias])

def adicionar_usuario(request)->[Usuario]:
    usuario = Usuario()
    usuario.nome = request.form['nome']
    usuario.email = request.form['email']
    usuario.nome_usuario = request.form['nomeUsuario']
    usuario.senha = request.form['senha']
    usuario.cpf = request.form['cpf']
    usuario.numero_telefone = request.form['numero_telefone']
    usuario.foto = request.form['foto']
    usuario.media_avaliacao = request.form['media_avaliacao']
    usuario.save()
    return usuario

if __name__ == '__main__':
    """Quando esse arquivo for executado como main será criada as tabelas de banco de dados"""

    def delete_banco_dados():
        path = os.getcwd()
        diretorio = os.listdir(path)
        for file in diretorio:
            if file == "ride_dote.db":
                os.remove(file)

    def existe_banco_dados() -> bool:
        """verifica se existe um arquivo de banco de dados com nome ride_dote.db"""
        path = os.getcwd()
        diretorio = os.listdir(path)
        for file in diretorio:
            if file == "ride_dote.db":
                return True
        return False

    if existe_banco_dados():
        delete_banco_dados()
    create_tables()
    populate_db.criar_informacoes()
