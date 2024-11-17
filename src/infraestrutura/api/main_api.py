import os
import logging
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from servicos.reserva_servico import ReservaServico
from servicos.usuario_servico import UsuarioServico
from casos_de_uso.reserva_caso_de_uso import ReservaCasosDeUso
from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.sqlite_reserva_repositorio import SQLiteReservaRepositorio
from repositorios.sqlite_usuario_repositorio import SQLiteUsuarioRepositorio
from infraestrutura.seguranca.criptografia import hash_senha, verificar_senha
from casos_de_uso.area_reservavel_caso_de_uso import AreaReservavelCasosDeUso
from repositorios.area_reservavel_repositorio import AreaReservavelRepositorio
from interfaces.dtos.models import AreaReservavelModel, AtualizarDisponibilidadeModel, LoginModel, MoradorModel, MoradorModeloResposta, ReservaModel, VisitanteModel

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

repositorio_usuario = SQLiteUsuarioRepositorio(connector)
casos_de_uso_usuario = UsuarioCasosDeUso(repositorio_usuario)
servico = UsuarioServico(casos_de_uso_usuario)

repositorio_reserva = SQLiteReservaRepositorio(connector)
casos_de_uso_reserva = ReservaCasosDeUso(repositorio_reserva, usuario_repositorio=repositorio_usuario)
servico_reserva = ReservaServico(casos_de_uso_reserva)

repositorio_area_reservavel = AreaReservavelRepositorio(connector)
casos_de_uso_area_reservavel = AreaReservavelCasosDeUso(repositorio_area_reservavel)


@app.post("/moradores/cadastro/")
def criar_morador(morador: MoradorModel):
    try:
        senha_criptografada = hash_senha(morador.senha)
        servico.adicionar_morador(
            nome=morador.nome,
            email=morador.email,
            telefone=morador.telefone,
            cpf=morador.cpf,
            data_nascimento=morador.data_nascimento,
            senha=senha_criptografada
        )
        return {"mensagem": "Morador criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/moradores/login/")
def login(login: LoginModel):
    try:
        morador = servico.buscar_morador_por_email(login.email)
        if morador and verificar_senha(login.senha, morador.senha):
            return {"mensagem": "Login realizado com sucesso"}
        else:
            raise HTTPException(status_code=401, detail="Credenciais inválidas - https://http.cat/401")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/moradores/listar/", response_model=List[MoradorModeloResposta])
def obter_moradores():
    try:
        moradores = servico.obter_moradores()
        return [MoradorModeloResposta(
            nome=morador.nome,
            email=morador.email,
            telefone=morador.telefone,
            cpf=morador.cpf,
            data_nascimento=morador.data_nascimento,
            senha=morador.senha
        ) for morador in moradores]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Visitantes


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
def obter_visitantes(response_model=List[VisitanteModel]):
    try:
        visitantes = servico.obter_visitantes()
        return [VisitanteModel(
            nome=visitante.nome,
            cpf=visitante.cpf,
            telefone=visitante.telefone,
            veiculo=visitante.veiculo,
            data_entrada=visitante.data_entrada,
            data_saida=visitante.data_saida
        ) for visitante in visitantes
        ]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Reserva de áreas comuns


    
    
    
@app.post("/reservar/agendar/")
def criar_reserva(reserva: ReservaModel):
    try:
        morador = servico.obter_morador_por_cpf(reserva.cpf_morador)
        if morador is None:
            raise HTTPException(status_code=404, detail="Morador não encontrado")
        
        area_reservavel = casos_de_uso_area_reservavel.obter_area_reservavel_por_nome_aproximado(reserva.area_reserva)
        if not area_reservavel.disponivel:
            raise HTTPException(status_code=400, detail=f"Área não está disponível. Reservada por {area_reservavel.reservado_por} em {area_reservavel.data_reserva}")
        
        # Atualiza a disponibilidade da área reservável para false se reservado_por não estiver vazio
        if reserva.reservado_por:
            casos_de_uso_area_reservavel.atualizar_disponibilidade_area_reservavel(area_reservavel.id, False)
        
        servico_reserva.adicionar_reserva(
            id_morador=morador.id,
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



@app.delete("/reservar/cancelar/{id_reserva}")
def cancelar_reserva(id_reserva: int):
    try:
        reserva = servico_reserva.obter_reserva_por_id(id_reserva)
        if reserva is None:
            raise HTTPException(status_code=404, detail="Reserva não encontrada")

        # Atualiza a disponibilidade da área reservável para true
        area_reservavel = casos_de_uso_area_reservavel.obter_area_reservavel_por_nome_aproximado(reserva.local_reserva)
        casos_de_uso_area_reservavel.atualizar_disponibilidade_area_reservavel(area_reservavel.id, True)

        servico_reserva.cancelar_reserva(id_reserva)
        return {"mensagem": "Reserva cancelada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@app.put("/areas_reservaveis/{nome_area}/disponibilidade/")
def atualizar_disponibilidade_area_reservavel(nome_area: str, disponibilidade: AtualizarDisponibilidadeModel):
    try:
        casos_de_uso_area_reservavel.atualizar_disponibilidade_area_reservavel(nome_area, disponibilidade.disponivel)
        return {"mensagem": "Disponibilidade da área reservável atualizada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/areas_reservaveis/cadastro/")
def criar_area_reservavel(area_reservavel: AreaReservavelModel):
    try:
        casos_de_uso_area_reservavel.adicionar_area_reservavel(
            disponivel=area_reservavel.disponivel,
            nome_area=area_reservavel.nome_area,
            horario_funcionamento=area_reservavel.horario_funcionamento,
            reservado_por=area_reservavel.reservado_por
        )
        return {"mensagem": "Área reservável criada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/areas_reservaveis/listar/", response_model=List[AreaReservavelModel])
def obter_areas_reservaveis():
    try:
        areas_reservaveis = casos_de_uso_area_reservavel.obter_areas_reservaveis()
        return [AreaReservavelModel(
            disponivel=area.disponivel,
            nome_area=area.nome_area,
            horario_funcionamento=area.horario_funcionamento,
            reservado_por=area.reservado_por if area.reservado_por else None
        ) for area in areas_reservaveis]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/areas_reservaveis/{nome}/", response_model=AreaReservavelModel)
def obter_area_reservavel_por_nome(nome: str):
    try:
        area_reservavel = casos_de_uso_area_reservavel.obter_area_reservavel_por_nome(nome)
        return AreaReservavelModel(
            disponivel=area_reservavel.disponivel,
            nome_area=area_reservavel.nome_area,
            horario_funcionamento=area_reservavel.horario_funcionamento,
            reservado_por=area_reservavel.reservado_por
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/areas_reservaveis/disponibilidade/{disponibilidade}/", response_model=List[AreaReservavelModel])
def obter_areas_reservaveis_por_disponibilidade(disponibilidade: bool):
    try:
        areas_reservaveis = casos_de_uso_area_reservavel.obtendo_areas_reservaveis_por_disponibilidade(disponibilidade)
        return [AreaReservavelModel(
            disponivel=area.disponivel,
            nome_area=area.nome_area,
            horario_funcionamento=area.horario_funcionamento,
            reservado_por=area.reservado_por if area.reservado_por else None
        ) for area in areas_reservaveis]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))