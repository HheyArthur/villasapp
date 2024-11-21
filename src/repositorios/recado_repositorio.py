from entidades.recado import Recado

class RecadoRepositorio:
    def __init__(self, connector):
        self.connector = connector
        self.connector.execute("""
            CREATE TABLE IF NOT EXISTS recados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conteudo TEXT NOT NULL,
                cpf_autor TEXT NOT NULL
            )
        """)

    def adicionar_recado(self, recado: Recado):
        query = "INSERT INTO recados (conteudo, cpf_autor) VALUES (?, ?)"
        params = (recado.conteudo, recado.cpf_autor)
        self.connector.execute(query, params)
        recado.id = self.connector.cursor.lastrowid

    def obter_recados(self):
        query = "SELECT id, conteudo, cpf_autor FROM recados"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [Recado(id=row[0], conteudo=row[1], cpf_autor=row[2]) for row in rows]

    def deletar_recado(self, id: int):
        query = "DELETE FROM recados WHERE id = ?"
        self.connector.execute(query, (id,))