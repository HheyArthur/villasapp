import os
import logging
from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from servicos.reserva_servico import ReservaServico
from servicos.usuario_servico import UsuarioServico
from repositorios.recado_repositorio import RecadoRepositorio
from casos_de_uso.recado_casos_de_uso import RecadoCasosDeUso
from casos_de_uso.reserva_caso_de_uso import ReservaCasosDeUso
from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from infraestrutura.connectors.sqlite_connector import SQLiteConnector
from repositorios.sqlite_reserva_repositorio import SQLiteReservaRepositorio
from repositorios.sqlite_usuario_repositorio import SQLiteUsuarioRepositorio
from infraestrutura.seguranca.criptografia import hash_senha, verificar_senha
from casos_de_uso.area_reservavel_caso_de_uso import AreaReservavelCasosDeUso
from repositorios.area_reservavel_repositorio import AreaReservavelRepositorio
from interfaces.dtos.models import AreaReservavelModel, AtualizarDisponibilidadeModel, AtualizarHorariosVisitanteModel, LoginModel, MoradorModel, MoradorModeloResposta, RecadoModel, RecadoRespostaModel, ReservaModel, VisitanteModel

app = FastAPI()

origins = [
    "*",  # Permitir todos os hosts
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

repositorio_recado = RecadoRepositorio(connector)
casos_de_uso_recado = RecadoCasosDeUso(repositorio_recado)


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
            numero_apartamento=morador.numero_apartamento,
            senha=morador.senha
        ) for morador in moradores]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/moradores/pesquisar/", response_model=List[MoradorModeloResposta])
def pesquisar_moradores(nome: Optional[str] = None, email: Optional[str] = None, cpf: Optional[str] = None, data_nascimento: Optional[str] = None):
    try:
        moradores = servico.pesquisar_moradores(nome, email, cpf, data_nascimento)
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
    
@app.get("/reservas/listar/")
def obter_reservas():
    try:
        reserva_servico = ReservaServico(casos_de_uso_reserva)
        reservas = reserva_servico.obter_reservas()
        return reservas
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/recados/listar/", response_model=List[RecadoRespostaModel])
def obter_recados():
    try:
        recados = casos_de_uso_recado.obter_recados()
        recados_resposta = []
        for recado in recados:
            nome_autor = servico.obter_nome_por_cpf(recado.cpf_autor)
            recados_resposta.append(RecadoRespostaModel(
                conteudo=recado.conteudo,
                nome_autor=nome_autor
            ))
        return recados_resposta
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/recados/cadastro/")
def criar_recado(recado: RecadoModel):
    try:
        if len(recado.conteudo) > 300:
            raise HTTPException(status_code=400, detail="O recado não pode ter mais de 300 caracteres")
        casos_de_uso_recado.adicionar_recado(recado.conteudo, recado.cpf_autor)
        return {"mensagem": "Recado criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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
            numero_apartamento=morador.numero_apartamento,
            senha=senha_criptografada
        )
        return {"mensagem": "Morador criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/moradores/login/")
def login(morador: LoginModel):
    try:
        morador_db = servico.buscar_morador_por_email(morador.email)
        if not morador_db or not verificar_senha(morador.senha, morador_db.senha.encode('utf-8')):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
        return {"mensagem": "Login realizado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.put("/areas_reservaveis/{nome_area}/disponibilidade/")
def atualizar_disponibilidade_area_reservavel(nome_area: str, disponibilidade: AtualizarDisponibilidadeModel):
    try:
        casos_de_uso_area_reservavel.atualizar_disponibilidade_area_reservavel(nome_area, disponibilidade.disponivel)
        return {"mensagem": "Disponibilidade da área reservável atualizada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/visitantes/atualizar_horarios/{cpf}")
def atualizar_horarios_visitante(cpf: str, horarios: AtualizarHorariosVisitanteModel):
    try:
        servico.atualizar_horarios_visitante(cpf, horarios.data_entrada, horarios.data_saida)
        return {"mensagem": "Horários do visitante atualizados com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.delete("/recados/deletar/{id}")
def deletar_recado(id: int):
    try:
        casos_de_uso_recado.deletar_recado(id)
        return {"mensagem": "Recado deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.delete("/reserva/cancelar/{id_reserva}")
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

@app.delete("/moradores/deletar/")
def deletar_moradores(cpf_list: List[str]):
    try:
        for cpf in cpf_list:
            servico.deletar_morador_por_cpf(cpf)
        return {"mensagem": "Moradores deletados com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))