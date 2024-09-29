from entidades.entidade_reserva import Reserva
from casos_de_uso.reserva_caso_de_uso import ReservaCasosDeUso

class ReservaServico:
    def __init__(self, reserva_repositorio: ReservaCasosDeUso):
        self.casos_de_uso = reserva_repositorio

    def adicionar_reserva(self, id_reserva, id_morador, data_reserva, area_reserva):
        reserva = Reserva(id_reserva, id_morador, data_reserva, area_reserva)
        self.casos_de_uso.adicionar_reserva(reserva)

    def obter_reservas(self):
        return self.casos_de_uso.obter_reservas()