from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante

class UsuarioRepositorio:
    def __init__(self):
        self.moradores = []
        self.visitantes = []

    def adicionar_morador(self, morador: Morador):
        self.moradores.append(morador)

    def adicionar_visitante(self, visitante: UsuarioVisitante):
        self.visitantes.append(visitante)

    def obter_moradores(self):
        return self.moradores

    def obter_visitantes(self):
        return self.visitantes