from entidades.usuario_morador import Morador
from entidades.entidade_reserva import Reserva
from repositorios.usuario_repositorio import UsuarioRepositorio
from repositorios.reservas_repositorio import ReservaRepositorio


class ReservaCasosDeUso:
    def __init__(self, repositorio: ReservaRepositorio, usuario_repositorio: UsuarioRepositorio):
        self.repositorio = repositorio
        self.usuario_repositorio = usuario_repositorio

    def adicionar_reserva(self, reserva):
        self.repositorio.adicionar_reserva(reserva)

    def obter_reservas(self):
        return self.repositorio.obter_reservas()
    
    def cancelar_reserva(self, id_reserva):
        self.repositorio.cancelar_reserva(id_reserva)
    
    def obter_reserva_por_id(self, id_reserva: int) -> Reserva:
        return self.repositorio.obter_reserva_por_id(id_reserva)

    def obter_morador_por_id(self, id_morador: int) -> Morador:
        return self.usuario_repositorio.obter_morador_por_id(id_morador)