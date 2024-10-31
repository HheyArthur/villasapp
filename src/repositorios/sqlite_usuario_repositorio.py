from entidades.usuario_visitante import UsuarioVisitante
from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.usuario_repositorio import UsuarioRepositorio
from entidades.usuario_morador import Morador

class SQLiteUsuarioRepositorio(UsuarioRepositorio):
    def __init__(self, connector: SQLiteConnector):
        self.connector = connector
        self.connector.create_tables()

    def adicionar_morador(self, morador: Morador):
        query = "INSERT INTO moradores (nome, email, telefone, cpf, data_nascimento, senha) VALUES (?, ?, ?, ?, ?, ?)"
        params = (morador.nome, morador.email, morador.telefone, morador.cpf, morador.data_nascimento, morador.senha)
        self.connector.execute(query, params)

    def obter_moradores(self):
        query = "SELECT * FROM moradores"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [Morador(*row) for row in rows]
    
    def adicionar_visitante(self, visitante: UsuarioVisitante):
        query = "INSERT INTO visitantes (nome, cpf, telefone, veiculo, data_entrada, data_saida) VALUES (?, ?, ?, ?, ?, ?)"
        params = (visitante.nome, visitante.cpf, visitante.telefone, visitante.veiculo, visitante.data_entrada, visitante.data_saida)
        self.connector.execute(query, params)

    def obter_visitantes(self):
        query = "SELECT * FROM visitantes"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [UsuarioVisitante(*row) for row in rows]