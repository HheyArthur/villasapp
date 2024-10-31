import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from casos_de_uso.reserva_caso_de_uso import ReservaCasosDeUso
from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.sqlite_reserva_repositorio import SQLiteReservaRepositorio
from repositorios.sqlite_usuario_repositorio import SQLiteUsuarioRepositorio
from servicos.usuario_servico import UsuarioServico
from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from servicos.reserva_servico import ReservaServico


app = FastAPI()

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Caminho do banco de dados
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'villasapp_base.db')
logging.info(f"Caminho do banco de dados: {db_path}")

# Cria o diretório se não existir
os.makedirs(os.path.dirname(db_path), exist_ok=True)
logging.info(f"Diretório do banco de dados criado/verificado: {os.path.dirname(db_path)}")

# Inicializa o conector e o repositório
connector = SQLiteConnector(db_path)
repositorio = SQLiteUsuarioRepositorio(connector)
casos_de_uso = UsuarioCasosDeUso(repositorio)
servico = UsuarioServico(casos_de_uso)

repositorio_reserva = SQLiteReservaRepositorio(connector)
casos_de_uso_reserva = ReservaCasosDeUso(repositorio)
servico_reserva = ReservaServico(casos_de_uso_reserva)

# Moradores

class MoradorModel(BaseModel):
    nome: str
    email: str
    telefone: str
    cpf: str
    data_nascimento: str
    senha: str

@app.post("/moradores/cadastro/")
def criar_morador(morador: MoradorModel):
    try:
        servico.adicionar_morador(
            nome=morador.nome,
            email=morador.email,
            telefone=morador.telefone,
            cpf=morador.cpf,
            data_nascimento=morador.data_nascimento,
            senha=morador.senha
        )
        return {"mensagem": "Morador criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/moradores/listar/")
def obter_moradores():
    try:
        moradores = servico.obter_moradores()
        return moradores
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Visitantes

class VisitanteModel(BaseModel):
    nome: str
    cpf: str
    telefone: str
    veiculo: str
    data_entrada: str
    data_saida: str

@app.post("/visitantes/cadastro/")
def criar_visitante(visitante: VisitanteModel):
    try:
        servico.adicionar_visitante(
            nome=visitante.nome,
            cpf=visitante.cpf,
            telefone=visitante.telefone,
            veiculo=visitante.veiculo,
            data_entrada=visitante.data_entrada,
            data_saida=visitante.data_saida
        )
        return {"mensagem": "Visitante criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/visitantes/listar/")
def obter_visitantes():
    try:
        visitantes = servico.obter_visitantes()
        return visitantes
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Reserva de áreas comuns

class ReservaModel(BaseModel):
    id_reserva: int
    id_morador: int
    data_reserva: str
    area_reserva: str
    
@app.post("/reservar/agendar/")
def criar_reserva(reserva: ReservaModel):
    try:
        reserva_servico = ReservaServico(casos_de_uso_reserva)
        reserva_servico.adicionar_reserva(
            id_reserva=reserva.id_reserva,
            id_morador=reserva.id_morador,
            data_reserva=reserva.data_reserva,
            area_reserva=reserva.area_reserva
        )
        return {"mensagem": "Reserva criada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/reservas/listar/")
def obter_reservas():
    try:
        reserva_servico = ReservaServico(casos_de_uso_reserva)
        reservas = reserva_servico.obter_reservas()
        return reservas
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))