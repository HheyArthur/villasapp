import pytest
from src.repositorios.usuario_repositorio import UsuarioRepositorio
from src.entidades.usuario_morador import Morador
from src.entidades.usuario_visitante import UsuarioVisitante

@pytest.fixture
def repositorio():
    return UsuarioRepositorio()

def test_adicionar_morador(repositorio):
    morador = Morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    repositorio.adicionar_morador(morador)
    assert morador in repositorio.moradores

def test_adicionar_visitante(repositorio):
    visitante = UsuarioVisitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    repositorio.adicionar_visitante(visitante)
    assert visitante in repositorio.visitantes

def test_obter_moradores(repositorio):
    morador = Morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    repositorio.adicionar_morador(morador)
    moradores = repositorio.obter_moradores()
    assert moradores == [morador]

def test_obter_visitantes(repositorio):
    visitante = UsuarioVisitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    repositorio.adicionar_visitante(visitante)
    visitantes = repositorio.obter_visitantes()
    assert visitantes == [visitante]