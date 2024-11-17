from entidades.entidade_reserva import Reserva
from casos_de_uso.reserva_caso_de_uso import ReservaCasosDeUso

class ReservaServico:
    def __init__(self, reserva_repositorio: ReservaCasosDeUso):
        self.casos_de_uso = reserva_repositorio

    def adicionar_reserva(self, id_morador, data_reserva, area_reserva):
        morador = self.casos_de_uso.obter_morador_por_id(id_morador)
        reserva = Reserva(id_morador=id_morador, data_reserva=data_reserva, area_reserva=area_reserva, nome_morador=morador.nome)
        self.casos_de_uso.adicionar_reserva(reserva)

    def obter_reservas(self):
        return self.casos_de_uso.obter_reservas()

    def cancelar_reserva(self, id_reserva: int):
        self.casos_de_uso.cancelar_reserva(id_reserva)

    def obter_reserva_por_id(self, id_reserva: int) -> Reserva:
        return self.casos_de_uso.obter_reserva_por_id(id_reserva)