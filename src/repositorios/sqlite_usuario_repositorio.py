from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from usuario_repositorio import UsuarioRepositorio
from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante

class SQLiteUsuarioRepositorio(UsuarioRepositorio):
    def __init__(self, connector: SQLiteConnector):
        self.connector = connector
        self.create_tables()

    def create_tables(self):
        conn = self.connector.get_connection()
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS moradores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    cpf TEXT
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS visitantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    cpf TEXT,
                    telefone TEXT,
                    veiculo TEXT,
                    data_entrada TEXT,
                    data_saida TEXT
                )
            ''')

    def adicionar_morador(self, morador: Morador):
        conn = self.connector.get_connection()
        with conn:
            conn.execute('''
                INSERT INTO moradores (nome, cpf) VALUES (?, ?)
            ''', (morador.nome, morador.cpf))

    def adicionar_visitante(self, visitante: UsuarioVisitante):
        conn = self.connector.get_connection()
        with conn:
            conn.execute('''
                INSERT INTO visitantes (nome, cpf, telefone, veiculo, data_entrada, data_saida)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (visitante.nome, visitante.cpf, visitante.telefone, visitante.veiculo, visitante.data_entrada, visitante.data_saida))

    def obter_moradores(self):
        conn = self.connector.get_connection()
        with conn:
            cursor = conn.execute('SELECT nome, cpf FROM moradores')
            return [Morador(nome=row[0], cpf=row[1]) for row in cursor.fetchall()]

    def obter_visitantes(self):
        conn = self.connector.get_connection()
        with conn:
            cursor = conn.execute('SELECT nome, cpf, telefone, veiculo, data_entrada, data_saida FROM visitantes')
            return [UsuarioVisitante(nome=row[0], cpf=row[1], telefone=row[2], veiculo=row[3], data_entrada=row[4], data_saida=row[5]) for row in cursor.fetchall()]