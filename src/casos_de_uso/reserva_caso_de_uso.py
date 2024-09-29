from repositorios.reservas_repositorio import ReservaRepositorio

class ReservaCasosDeUso:
    def __init__(self, repositorio: ReservaRepositorio):
        self.repositorio = repositorio

    def adicionar_reserva(self, reserva):
        self.repositorio.adicionar_reserva(reserva)

    def obter_reservas(self):
        return self.repositorio.obter_reservas()
    
    def cancelar_reserva(self, id_reserva):
        self.repositorio.cancelar_reserva(id_reserva)