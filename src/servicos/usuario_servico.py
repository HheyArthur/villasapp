from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante

class UsuarioServico:
    def __init__(self, casos_de_uso: UsuarioCasosDeUso):
        self.casos_de_uso = casos_de_uso

    def adicionar_morador(self, nome, email, telefone, cpf, data_nascimento, senha):
        morador = Morador(nome, email, telefone, cpf, data_nascimento, senha)
        self.casos_de_uso.adicionar_morador(morador)

    def adicionar_visitante(self, nome, cpf, telefone, veiculo, data_entrada, data_saida):
        visitante = UsuarioVisitante(nome, cpf, telefone, veiculo, data_entrada, data_saida)
        self.casos_de_uso.adicionar_visitante(visitante)

    def obter_moradores(self):
        return self.casos_de_uso.obter_moradores()

    def obter_visitantes(self):
        return self.casos_de_uso.obter_visitantes()