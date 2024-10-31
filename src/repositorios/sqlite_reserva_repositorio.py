from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.reservas_repositorio import ReservaRepositorio
from entidades.entidade_reserva import Reserva

class SQLiteReservaRepositorio(ReservaRepositorio):
    def __init__(self, connector: SQLiteConnector):
        self.connector = connector
        self.connector.create_tables()
    
    def adicionar_reserva(self, reserva: Reserva):
        query = "INSERT INTO reservas (id_reserva, id_morador, data_reserva, area_reserva) VALUES (?, ?, ?, ?)"
        params = (reserva.id_reserva, reserva.id_morador, reserva.data_reserva, reserva.area_reserva)
        self.connector.execute(query, params)
        
    def obter_reservas(self):
        query = "SELECT * FROM reservas"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [Reserva(*row) for row in rows]