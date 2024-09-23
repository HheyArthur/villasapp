import sys
import os
import pytest

from src.casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from src.repositorios.usuario_repositorio import UsuarioRepositorio
from src.entidades.usuario_morador import Morador
from src.entidades.usuario_visitante import UsuarioVisitante

@pytest.fixture
def casos_de_uso():
    repositorio = UsuarioRepositorio()
    return UsuarioCasosDeUso(repositorio)

def test_adicionar_morador(casos_de_uso):
    morador = Morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    casos_de_uso.adicionar_morador(morador)
    assert morador in casos_de_uso.repositorio.moradores

def test_adicionar_visitante(casos_de_uso):
    visitante = UsuarioVisitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    casos_de_uso.adicionar_visitante(visitante)
    assert visitante in casos_de_uso.repositorio.visitantes

def test_obter_moradores(casos_de_uso):
    morador = Morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    casos_de_uso.adicionar_morador(morador)
    moradores = casos_de_uso.obter_moradores()
    assert moradores == [morador]

def test_obter_visitantes(casos_de_uso):
    visitante = UsuarioVisitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    casos_de_uso.adicionar_visitante(visitante)
    visitantes = casos_de_uso.obter_visitantes()
    assert visitantes == [visitante]
import sys
import os

import pytest
from casos_de_uso.usuario_casos_de_uso import UsuarioCasosDeUso
from repositorios.usuario_repositorio import UsuarioRepositorio
from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante

@pytest.fixture
def casos_de_uso():
    repositorio = UsuarioRepositorio()
    return UsuarioCasosDeUso(repositorio)

def test_adicionar_morador(casos_de_uso):
    morador = Morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    casos_de_uso.adicionar_morador(morador)
    assert morador in casos_de_uso.repositorio.moradores

def test_adicionar_visitante(casos_de_uso):
    visitante = UsuarioVisitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    casos_de_uso.adicionar_visitante(visitante)
    assert visitante in casos_de_uso.repositorio.visitantes

def test_obter_moradores(casos_de_uso):
    morador = Morador("Nome", "email@example.com", "123456789", "123.456.789-00", "01/01/2000", "senha123")
    casos_de_uso.adicionar_morador(morador)
    moradores = casos_de_uso.obter_moradores()
    assert moradores == [morador]

def test_obter_visitantes(casos_de_uso):
    visitante = UsuarioVisitante("Nome", "123.456.789-00", "123456789", "Carro", "01/01/2023", "02/01/2023")
    casos_de_uso.adicionar_visitante(visitante)
    visitantes = casos_de_uso.obter_visitantes()
    assert visitantes == [visitante]