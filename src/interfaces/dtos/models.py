from typing import Optional
from pydantic import BaseModel

class MoradorModel(BaseModel):
    nome: str
    email: str
    telefone: str
    cpf: str
    data_nascimento: str
    senha: str

class MoradorModeloResposta(BaseModel):
    nome: str
    email: str
    telefone: str
    cpf: str
    data_nascimento: str
    senha: str

class VisitanteModel(BaseModel):
    nome: str
    cpf: str
    telefone: str
    veiculo: str
    data_entrada: str
    data_saida: str
    
class ReservaModel(BaseModel):
    cpf_morador: str
    data_reserva: str
    area_reserva: str
    reservado_por: str = None
    data_reserva: str = None
    
class AreaReservavelModel(BaseModel):
    disponivel: bool
    nome_area: str
    horario_funcionamento: str
    reservado_por: Optional[str] = None

class AtualizarDisponibilidadeModel(BaseModel):
    disponivel: bool
    
# Modelo para login
class LoginModel(BaseModel):
    email: str
    senha: str