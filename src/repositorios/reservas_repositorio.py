from entidades.entidade_reserva import Reserva

class ReservaRepositorio:
    def __init__(self):
        self.reservas = []

    def adicionar_reserva(self, reserva: Reserva):
        self.reservas.append(reserva)

    def obter_reservas(self):
        return self.reservas
    
    def cancelar_reserva(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                self.reservas.remove(reserva)
                return True
        return False