from repositorios.usuario_repositorio import UsuarioRepositorio

class UsuarioCasosDeUso:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def adicionar_morador(self, morador):
        self.repositorio.adicionar_morador(morador)

    def adicionar_visitante(self, visitante):
        self.repositorio.adicionar_visitante(visitante)

    def obter_moradores(self):
        return self.repositorio.obter_moradores()

    def obter_visitantes(self):
        return self.repositorio.obter_visitantes()