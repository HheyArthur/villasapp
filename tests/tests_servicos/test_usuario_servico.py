import pytest
from src.servicos.usuario_servico import UsuarioServico
from src.casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from src.repositorios.usuario_repositorio import UsuarioRepositorio

@pytest.fixture
def servico():
    repositorio = UsuarioRepositorio()
    casos_de_uso = UsuarioCasosDeUso(repositorio)
    return UsuarioServico(casos_de_uso)

def test_adicionar_morador(servico):
    servico.adicionar_morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    moradores = servico.obter_moradores()
    assert len(moradores) == 1
    assert moradores[0].nome == "Nome"

def test_adicionar_visitante(servico):
    servico.adicionar_visitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    visitantes = servico.obter_visitantes()
    assert len(visitantes) == 1
    assert visitantes[0].nome == "Nome"

def test_obter_moradores(servico):
    servico.adicionar_morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    moradores = servico.obter_moradores()
    assert len(moradores) == 1
    assert moradores[0].nome == "Nome"

def test_obter_visitantes(servico):
    servico.adicionar_visitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    visitantes = servico.obter_visitantes()
    assert len(visitantes) == 1
    assert visitantes[0].nome == "Nome"