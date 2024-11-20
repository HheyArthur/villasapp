import sqlite3
import logging

class SQLiteConnector:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        logging.info(f"Conectado ao banco de dados em: {database}")

    def execute(self, query, params=None):
        try:
            logging.info(f"Executando query: {query} | Params: {params}")
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            logging.info("Query executada com sucesso")
        except sqlite3.Error as e:
            logging.error(f"Erro ao executar a query: {e}")
            raise

    def fetchall(self):
        try:
            results = self.cursor.fetchall()
            logging.info(f"Resultados obtidos: {results}")
            return results
        except sqlite3.Error as e:
            logging.error(f"Erro ao obter resultados: {e}")
            raise
    
    def fetchone(self):
        try:
            result = self.cursor.fetchone()
            logging.info(f"Resultado obtido: {result}")
            return result
        except sqlite3.Error as e:
            logging.error(f"Erro ao obter resultado: {e}")
            raise
        
    def close(self):
        try:
            self.connection.close()
            logging.info("Conexão com o banco de dados fechada")
        except sqlite3.Error as e:
            logging.error(f"Erro ao fechar a conexão: {e}")
            raise

    def create_tables(self):
        create_table_query_moradores = """
        CREATE TABLE IF NOT EXISTS moradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cpf TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            senha TEXT NOT NULL
        );
        """
        create_table_query_visitantes = """
        CREATE TABLE IF NOT EXISTS visitantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            veiculo TEXT NOT NULL,
            data_entrada TEXT NOT NULL,
            data_saida TEXT NOT NULL
        );
        """
        create_table_query_reservas = """
        CREATE TABLE IF NOT EXISTS reservas (
            id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
            id_morador INTEGER NOT NULL,
            data_reserva TEXT NOT NULL,
            area_reserva TEXT NOT NULL,
            FOREIGN KEY (id_morador) REFERENCES moradores(id)
        );
        """
        create_table_query_areas_reservaveis = """
        CREATE TABLE IF NOT EXISTS areas_reservaveis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disponivel BOOLEAN NOT NULL,
            nome_area TEXT NOT NULL,
            horario_funcionamento TEXT NOT NULL,
            reservado_por TEXT,
            data_reserva TEXT
        );
        """
        self.execute(create_table_query_moradores)
        self.execute(create_table_query_visitantes)
        self.execute(create_table_query_reservas)
        self.execute(create_table_query_areas_reservaveis)