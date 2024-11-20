from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.reservas_repositorio import ReservaRepositorio
from entidades.entidade_reserva import Reserva

class SQLiteReservaRepositorio(ReservaRepositorio):
    def __init__(self, connector: SQLiteConnector):
        self.connector = connector
        self.connector.create_tables()
    
    def adicionar_reserva(self, reserva: Reserva):
        query = "INSERT INTO reservas (id_morador, data_reserva, area_reserva) VALUES (?, ?, ?)"
        params = (reserva.id_morador, reserva.data_reserva, reserva.local_reserva)
        self.connector.execute(query, params)
        reserva.id_reserva = self.connector.cursor.lastrowid

        # Atualiza o campo reservado_por e a disponibilidade da área reservável
        update_query = "UPDATE areas_reservaveis SET disponivel = ?, reservado_por = ?, data_reserva = ? WHERE LOWER(nome_area) LIKE LOWER(?)"
        update_params = (False, reserva.nome_morador, reserva.data_reserva, reserva.local_reserva)
        self.connector.execute(update_query, update_params)
        
    def obter_reservas(self):
        query = "SELECT id_reserva, id_morador, data_reserva, area_reserva FROM reservas"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [Reserva(id_reserva=row[0], id_morador=row[1], data_reserva=row[2], area_reserva=row[3]) for row in rows]

    def cancelar_reserva(self, id_reserva: int):
        # Obter a reserva antes de cancelar
        reserva = self.obter_reserva_por_id(id_reserva)
        
        query = "DELETE FROM reservas WHERE id_reserva = ?"
        self.connector.execute(query, (id_reserva,))

        # Atualiza o campo reservado_por e a disponibilidade da área reservável
        update_query = "UPDATE areas_reservaveis SET disponivel = ?, reservado_por = ?, data_reserva = ? WHERE nome_area = ?"
        update_params = (True, None, None, reserva.local_reserva)
        self.connector.execute(update_query, update_params)

    def obter_reserva_por_id(self, id_reserva: int) -> Reserva:
        query = "SELECT id_reserva, id_morador, data_reserva, area_reserva FROM reservas WHERE id_reserva = ?"
        self.connector.execute(query, (id_reserva,))
        row = self.connector.fetchone()
        if row:
            return Reserva(id_reserva=row[0], id_morador=row[1], data_reserva=row[2], area_reserva=row[3])
        else:
            raise ValueError("Reserva não encontrada")