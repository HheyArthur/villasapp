from typing import List, Optional
from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante

class UsuarioServico:
    def __init__(self, casos_de_uso: UsuarioCasosDeUso):
        self.casos_de_uso = casos_de_uso

    def adicionar_morador(self, nome, email, telefone, cpf, data_nascimento, numero_apartamento, senha):
        morador = Morador(nome, email, telefone, cpf, data_nascimento, senha, numero_apartamento)
        self.casos_de_uso.adicionar_morador(morador)

    def buscar_morador_por_email(self, email):
        return self.casos_de_uso.buscar_morador_por_email(email)

    def pesquisar_moradores(self, nome: Optional[str], email: Optional[str], cpf: Optional[str], data_nascimento: Optional[str]) -> List[Morador]:
        return self.casos_de_uso.pesquisar_moradores(nome, email, cpf, data_nascimento)

    def obter_moradores(self):
        return self.casos_de_uso.obter_moradores()

    def obter_morador_por_cpf(self, cpf):
        return self.casos_de_uso.obter_morador_por_cpf(cpf)
    
    def obter_nome_por_cpf(self, cpf: str) -> str:
        morador = self.casos_de_uso.obter_morador_por_cpf(cpf)
        return morador.nome
    
    def obter_morador_por_id(self, id: int) -> Morador:
        return self.casos_de_uso.obter_morador_por_id(id)
    
    def deletar_morador_por_cpf(self, cpf: str):
        self.casos_de_uso.deletar_morador_por_cpf(cpf)

    def adicionar_visitante(self, nome, cpf, telefone, veiculo, data_entrada, data_saida):
        visitante = UsuarioVisitante(nome, cpf, telefone, veiculo, data_entrada, data_saida)
        self.casos_de_uso.adicionar_visitante(visitante)

    def obter_visitantes(self):
        return self.casos_de_uso.obter_visitantes()
    
    def atualizar_horarios_visitante(self, cpf: str, data_entrada: str, data_saida: str):
        visitante = self.casos_de_uso.obter_visitante_por_cpf(cpf)
        if visitante:
            visitante.data_entrada = data_entrada
            visitante.data_saida = data_saida
            self.casos_de_uso.atualizar_visitante(visitante)
        else:
            raise ValueError("Visitante não encontrado")