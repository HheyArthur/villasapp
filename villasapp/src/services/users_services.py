from villasapp.src.entidades.usuario_morador import Morador
from villasapp.src.entidades.usuario_visitante import UsuarioVisitante
from villasapp.src.interfaces.metodos_usuarios import UsuarioInterface


class UsuarioService(UsuarioInterface):
    def get_morador_info(self, morador: Morador):
        return {
            "nome": morador.nome,
            "email": morador.email,
            "telefone": morador.telefone,
            "cpf": morador.cpf,
            "data_nascimento": morador.data_nascimento,
            "senha": morador.senha
        }

    def set_morador_info(self, morador: Morador, nome=None, email=None, telefone=None, cpf=None, data_nascimento=None, senha=None):
        if nome:
            morador.nome = nome
        if email:
            morador.email = email
        if telefone:
            morador.telefone = telefone
        if cpf:
            morador.cpf = cpf
        if data_nascimento:
            morador.data_nascimento = data_nascimento
        if senha:
            morador.senha = senha

    def get_visitante_info(self, visitante: UsuarioVisitante):
        return {
            "nome": visitante.nome,
            "cpf": visitante.cpf,
            "telefone": visitante.telefone,
            "veiculo": visitante.veiculo,
            "data_entrada": visitante.data_entrada,
            "data_saida": visitante.data_saida
        }

    def set_visitante_info(self, visitante: UsuarioVisitante, nome=None, cpf=None, telefone=None, veiculo=None, data_entrada=None, data_saida=None):
        if nome:
            visitante.nome = nome
        if cpf:
            visitante.cpf = cpf
        if telefone:
            visitante.telefone = telefone
        if veiculo:
            visitante.veiculo = veiculo
        if data_entrada:
            visitante.data_entrada = data_entrada
        if data_saida:
            visitante.data_saida = data_saida