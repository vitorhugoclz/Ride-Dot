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
    numero_vaga = IntegerField()
    data = DateTimeField()
    numero_telefone = CharField()
    valor = FloatField(default=0.0)
    usuario_ofertante = ForeignKeyField(Usuario)

class CidadesIntermediarias(ModelBase):
    cidade = CharField()
    rota_id = ForeignKeyField(Rota)


class RotaUsuario(ModelBase):
    usuario_id = ForeignKeyField(Usuario)
    rota_id = ForeignKeyField(Rota)
    vagas_pedidas = IntegerField(default=1)

def create_tables():
    """cria as tabelas do banco de dados"""
    database.connect()
    database.create_tables([Usuario, Avaliacao, Rota, CidadesIntermediarias, RotaUsuario])

##########################################################
# Funao para verificar login
##########################################################


def verificar_login(request:object):
    senha = str(request.form['senha'])
    nome_usuario = str(request.form['nome_usuario'])
    data = Usuario.select().where(Usuario.nome_usuario == nome_usuario)
    if data:
        if data[0].senha != senha:
            return None
        return data[0]
    return None

##########################################################
# Funcoes relacionados ao usuario
##########################################################
@database.atomic()
def adicionar_usuario(request:object)->Usuario:
    '''armazena um usuario no banco de dados'''
    usuario = Usuario()
    usuario.nome = request.form['nome']
    usuario.email = request.form['email']
    usuario.nome_usuario = request.form['nome_usuario']
    usuario.senha = request.form['senha']
    usuario.cpf = request.form['cpf']
    usuario.numero_telefone = request.form['numero_telefone']
    usuario.foto = None
    usuario.media_avaliacao = 0.0
    usuario.save()
    return usuario
##########################################################
# Fim das Funcoes relacionados ao usuario
##########################################################


##########################################################
# Funcoes adicionar rota
##########################################################
@database.atomic()
def adicionar_rota(request:object, usuario_ofertante)->Rota:
    '''' armazena uma rota no banco de dados '''
    rota = Rota()
    rota.cidade_destino = request.form['cidade_destino'].lower()
    rota.cidade_origem = request.form['cidade_origem'].lower()
    rota.data = request.form['data']
    rota.numero_telefone = request.form['telefone']
    rota.numero_vaga = request.form['numero_vagas']
    rota.valor = request.form['preco_viagem']
    rota.usuario_ofertante = usuario_ofertante
    rota.save()
    return rota
##########################################################
# fim funcoes adicionar rota
##########################################################


##########################################################
# funcoes buscar carona
##########################################################

def buscar_carona(request:object):
    def converteLista(data, cidade_destino):
        lista = list()
        for iten in data:
            if iten.cidade_destino == cidade_destino and iten.numero_vaga > 0:
                lista.append(iten)
        return lista
    cidade_origem = request.form['cidade_origem'].lower()
    cidade_destino =  request.form['cidade_destino'].lower()

    data = Rota.select().where(Rota.cidade_origem == cidade_origem)

    return converteLista(data, cidade_destino)

def salvar_inscricao_rota(id:int, usuario_id):
    '''comentario de inscricao'''
    data = Rota.select().where(Rota.id == id)
    if data:
        if data[0].numero_vaga > 0 and data[0].numero_vaga >= 1:
            data[0].numero_vaga = data[0].numero_vaga - 1
            data[0].save()
            rota_usuario = RotaUsuario()
            rota_usuario.rota_id = id
            rota_usuario.usuario_id = usuario_id
            rota_usuario.save()


def buscar_rota_inscrita(usuario_id):
    def fazer_lista_rota(data):
        lista = list()
        for i in data:
            iten = Rota.select().where(Rota.id == i.rota_id)
            for j in iten:
                lista.append(j)
        return lista
    data = RotaUsuario.select().where(RotaUsuario.usuario_id == usuario_id)
    data = fazer_lista_rota(data)
    return data


def buscar_rota_oferecida(usuario_ofertante):
    data = Rota().select().where(Rota.usuario_ofertante == usuario_ofertante)
    return data
##########################################################
# fim funcoes buscar carona
##########################################################

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

