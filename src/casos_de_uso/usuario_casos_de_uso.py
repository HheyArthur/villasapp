from repositorios.usuario_repositorio import UsuarioRepositorio


class UsuarioCasosDeUso:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def adicionar_morador(self, morador):
        self.repositorio.adicionar_morador(morador)

    def adicionar_visitante(self, visitante):
        self.repositorio.adicionar_visitante(visitante)

    def buscar_morador_por_email(self, email):
        return self.repositorio.buscar_morador_por_email(email)

    def obter_moradores(self):
        return self.repositorio.obter_moradores()

    def obter_morador_por_cpf(self, cpf):
        return self.repositorio.obter_morador_por_cpf(cpf)

    def obter_visitantes(self):
        return self.repositorio.obter_visitantes()