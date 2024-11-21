from repositorios.recado_repositorio import RecadoRepositorio
from entidades.recado import Recado

class RecadoCasosDeUso:
    def __init__(self, repositorio: RecadoRepositorio):
        self.repositorio = repositorio

    def adicionar_recado(self, conteudo, cpf_autor):
        recado = Recado(conteudo=conteudo, cpf_autor=cpf_autor)
        self.repositorio.adicionar_recado(recado)

    def obter_recados(self):
        return self.repositorio.obter_recados()

    def deletar_recado(self, id: int):
        self.repositorio.deletar_recado(id)