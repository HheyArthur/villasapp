from entidades.area_reservavel import AreaReservavel

class AreaReservavelRepositorio:
    def __init__(self, connector):
        self.connector = connector

    def adicionar_area_reservavel(self, area_reservavel: AreaReservavel):
        query = "INSERT INTO areas_reservaveis (disponivel, nome_area, horario_funcionamento, reservado_por, data_reserva) VALUES (?, ?, ?, ?, ?)"
        params = (area_reservavel.disponivel, area_reservavel.nome_area, area_reservavel.horario_funcionamento, area_reservavel.reservado_por, area_reservavel.data_reserva)
        self.connector.execute(query, params)
        area_reservavel.id = self.connector.cursor.lastrowid

    def obter_areas_reservaveis(self):
        query = "SELECT id, disponivel, nome_area, horario_funcionamento, reservado_por, data_reserva FROM areas_reservaveis"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [AreaReservavel(id=row[0], disponivel=row[1], nome_area=row[2], horario_funcionamento=row[3], reservado_por=row[4], data_reserva=row[5]) for row in rows]

    def obter_area_reservavel_por_nome(self, nome: str) -> AreaReservavel:
        query = "SELECT id, disponivel, nome_area, horario_funcionamento, reservado_por, data_reserva FROM areas_reservaveis WHERE id = ?"
        self.connector.execute(query, (nome,))
        row = self.connector.fetchone()
        if row:
            return AreaReservavel(id=row[0], disponivel=row[1], nome_area=row[2], horario_funcionamento=row[3], reservado_por=row[4], data_reserva=row[5])
        else:
            raise ValueError("Área reservável não encontrada")

    def obter_area_reservavel_por_nome_aproximado(self, nome: str) -> AreaReservavel:
        query = "SELECT id, disponivel, nome_area, horario_funcionamento, reservado_por, data_reserva FROM areas_reservaveis WHERE nome_area LIKE ?"
        self.connector.execute(query, (f"%{nome}%",))
        row = self.connector.fetchone()
        if row:
            return AreaReservavel(id=row[0], disponivel=row[1], nome_area=row[2], horario_funcionamento=row[3], reservado_por=row[4], data_reserva=row[5])
        else:
            raise ValueError("Área reservável não encontrada")

    def atualizar_disponibilidade_area_reservavel(self, id: int, disponivel: bool):
        query = "UPDATE areas_reservaveis SET disponivel = ? WHERE id = ?"
        self.connector.execute(query, (disponivel, id))
        
    def obtendo_areas_reservaveis_por_disponibilidade(self, disponibilidade: bool):
        query = "SELECT id, disponivel, nome_area, horario_funcionamento, reservado_por, data_reserva FROM areas_reservaveis WHERE disponivel = ?"
        self.connector.execute(query, (disponibilidade,))
        rows = self.connector.fetchall()
        return [AreaReservavel(id=row[0], disponivel=row[1], nome_area=row[2], horario_funcionamento=row[3], reservado_por=row[4], data_reserva=row[5]) for row in rows]
    
    def adicionar_coluna_data_reserva(self):
        query = "ALTER TABLE areas_reservaveis ADD COLUMN data_reserva TEXT"
        self.connector.execute(query)
    
    def atualizar_disponibilidade_area_reservavel(self, id: int, disponivel: bool):
        query = "UPDATE areas_reservaveis SET disponivel = ? WHERE id = ?"
        self.connector.execute(query, (disponivel, id))