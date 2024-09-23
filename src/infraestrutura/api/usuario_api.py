from fastapi import FastAPI
from servicos.usuario_servico import UsuarioServico
from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from repositorios.usuario_repositorio import UsuarioRepositorio

app = FastAPI()

repositorio = UsuarioRepositorio()
casos_de_uso = UsuarioCasosDeUso(repositorio)
servico = UsuarioServico(casos_de_uso)

@app.post("/moradores/")
def adicionar_morador(nome: str, email: str, telefone: str, cpf: str, data_nascimento: str, senha: str):
    servico.adicionar_morador(nome, email, telefone, cpf, data_nascimento, senha)
    return {"message": "Morador adicionado com sucesso"}

@app.post("/visitantes/")
def adicionar_visitante(nome: str, cpf: str, telefone: str, veiculo: str, data_entrada: str, data_saida: str):
    servico.adicionar_visitante(nome, cpf, telefone, veiculo, data_entrada, data_saida)
    return {"message": "Visitante adicionado com sucesso"}

@app.get("/moradores/")
def obter_moradores():
    return servico.obter_moradores()

@app.get("/visitantes/")
def obter_visitantes():
    return servico.obter_visitantes()