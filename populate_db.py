import bd

def inserir_usuarios(rows: list) -> None:
    """Insere todos os dados da constante USUARIOS"""
    bd.Usuario.insert_many(rows).execute()


def inserir_avaliacoes(rows: list) -> None:
    """Insere todos os dados da constante AVALIACAO"""
    bd.Avaliacao.insert_many(rows).execute()


def inserir_rota(rows: list) -> None:
    """Insere todos os dados da constante ROTA"""
    bd.Rota.insert_many(rows).execute()


def inserir_cidades_intermediarias(rows: list) -> None:
    """Insere todos os dados da constante CIDADES_INTERMEDIARIAS"""
    bd.CidadesIntermediarias.insert_many(rows).execute()


def inserir_rota_usuario(rows: list) -> None:
    bd.RotaUsuario.insert_many(rows).execute()


USUARIO = [{'id': 1, 'nome': 'vitor hugo', 'email': 'vitorhugoclz@email.com', 'nome_usuario': 'vitor',
                'senha': 'vitor', 'cpf': '999.999.999-99', 'numero_telefone': '19 999999999', 'media_avaliacao': 2.5},

            {'id': 2, 'nome': 'maria luiza', 'email': 'maria@email.com', 'nome_usuario': 'maria',
                'senha': 'maria', 'cpf': '888.888.888-88', 'numero_telefone': '35 999999999', 'media_avaliacao': 1.5},

            {'id': 3, 'nome': 'otavio augusto', 'email': 'otavio@email.com', 'nome_usuario': 'otavio',
                'senha': 'otavio', 'cpf': '777.777.777-77', 'numero_telefone': '35 77777777', 'media_avaliacao': 3.5},

            {'id': 4, 'nome': 'gustavo henrique', 'email': 'gustavo@email.com', 'nome_usuario': 'gustavo',
                'senha': 'gustavo', 'cpf': '666.666.666-66', 'numero_telefone': '19 77777777', 'media_avaliacao': 3.0},

            {'id': 5, 'nome': 'luiz gustavo', 'email': 'luiz@email.com', 'nome_usuario': 'luiz',
                'senha': 'luiz', 'cpf': '555.555.555-55', 'numero_telefone': '19 555555', 'media_avaliacao': 3.0},

            {'id': 6, 'nome': 'denis', 'email': 'denis@email.com', 'nome_usuario': 'denis',
                'senha': 'denis', 'cpf': '444.444.444-44', 'numero_telefone': '19 444444', 'media_avaliacao': 4.0},

            {'id': 7, 'nome': 'ariela', 'email': 'ariela@email.com', 'nome_usuario': 'ariela',
                'senha': 'ariela', 'cpf': '333.333.333-33', 'numero_telefone': '19 333333', 'media_avaliacao': 2.0},

            {'id': 8, 'nome': 'luana', 'email': 'luana@email.com', 'nome_usuario': 'luana',
                'senha': 'luana', 'cpf': '222.222.222-22', 'numero_telefone': '19 222222', 'media_avaliacao': 3.45},
            {'id': 9, 'nome': 'pedro', 'email': 'pedro@email.com', 'nome_usuario': 'pedro',
                'senha': 'pedro', 'cpf': '111.111.111-11', 'numero_telefone': '19 111111', 'media_avaliacao': 4.5}]

AVALIACAO = [{'nota': 2.5, 'comentario': 'gordo falante', 'data': '2019-12-14', 'usuario_id': 1},

             {'nota': 1.5, 'comentario': 'parece que usa cocaina', 'data': '2019-12-14', 'usuario_id': 2},

             {'nota': 3.5, 'comentario': 'moço respeitoso', 'data': '2019-12-14', 'usuario_id': 3},

             {'nota': 3.0, 'comentario': 'menino beyblade', 'data': '2019-12-14', 'usuario_id': 4},

             {'nota': 3.0, 'comentario': None, 'data': '2019-12-14', 'usuario_id': 5},

             {'nota': 4.0, 'comentario': 'deixa nois joga switch', 'data': '2019-12-14', 'usuario_id': 6},

             {'nota': 2.0, 'comentario': None,'data': '2019-12-14', 'usuario_id': 7},

             {'nota': 3.45, 'comentario': None,'data': '2019-12-14', 'usuario_id': 8},

             {'nota': 3.45, 'comentario': 'menino de deus', 'data': '2019-12-14', 'usuario_id': 9},

             {'nota': 2.5, 'comentario': 'gordo chato do caraio', 'data': '2019-12-14', 'usuario_id': 1}]

ROTA = [{'cidade_origem': 'alfenas', 'numero_vaga': 2, 'cidade_destino': 'tapiratiba',
         'data':'2019-12-14 12:00:00', 'numero_telefone': '19 999999999','usuario_ofertante': 1},

        {'cidade_origem': 'alfenas', 'numero_vaga': 3, 'cidade_destino': 'rio de janeiro',
         'data':'2019-12-14 17:35:00', 'numero_telefone': '19 111111','usuario_ofertante': 9},

        {'cidade_origem': 'alfenas', 'numero_vaga': 1, 'cidade_destino': 'pouso alegre',
         'data':'2019-12-14 17:35:00', 'numero_telefone': '19 444444','usuario_ofertante': 6}]

CIDADES_INTERMEDIARIAS = [{'cidade': 'guaxupe', 'rota_id': 1},
                          {'cidade': 'campos gerais', 'rota_id': 3}]
ROTA_USUARIO = [{'usuario_id': 2, 'rota_id': 1},
                {'usuario_id': 1, 'rota_id': 2},
                {'usuario_id': 4, 'rota_id': 2},
                {'usuario_id': 5, 'rota_id': 3}]

def criar_informacoes():
    inserir_usuarios(USUARIO)
    inserir_avaliacoes(AVALIACAO)
    inserir_rota(ROTA)
    inserir_cidades_intermediarias(CIDADES_INTERMEDIARIAS)
    inserir_rota_usuario(ROTA_USUARIO)


if __name__ == '__main__':
    criar_informacoes()
