import os
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
    email = CharField()
    nomeUsuario = CharField()
    foto = CharField()
    senha = CharField()
    cpf = CharField()
    numero_telefone = CharField(null=True)


class Avaliacao(ModelBase):
    nota = FloatField()
    comentario = CharField()
    data = DateField()
    usuario_id = ForeignKeyField(Usuario)


class Rota(ModelBase):
    cidade_origem = CharField()
    cidade_destino = CharField()


class CidadesIntermediarias(ModelBase):
    cidade = CharField()
    rota_id = ForeignKeyField(Rota)


def create_tables():
    """cria as tabelas do banco de dados"""
    database.connect()
    database.create_tables([Usuario, Avaliacao, Rota, CidadesIntermediarias])


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
