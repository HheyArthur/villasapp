from abc import ABC, abstractmethod
from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante

class UsuarioInterface(ABC):
    @abstractmethod
    def get_morador_info(self, morador: Morador):
        pass

    @abstractmethod
    def set_morador_info(self, morador: Morador, nome=None, email=None, telefone=None, cpf=None, data_nascimento=None, senha=None):
        pass

    @abstractmethod
    def get_visitante_info(self, visitante: UsuarioVisitante):
        pass

    @abstractmethod
    def set_visitante_info(self, visitante: UsuarioVisitante, nome=None, cpf=None, telefone=None, veiculo=None, data_entrada=None, data_saida=None):
        pass