import sqlite3

class SQLiteConnector:
    def __init__(self, db_path='usuarios.db'):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)
