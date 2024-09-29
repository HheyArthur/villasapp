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