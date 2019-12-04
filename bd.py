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


def create_tables():
    """cria as tabelas do banco de dados"""
    database.connect()
    database.create_tables([Usuario])


if __name__ == '__main__':
    ''' Quando esse arquivo for executado como main será criada as tabelas de banco de dados '''
    create_tables()
