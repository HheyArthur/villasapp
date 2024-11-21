from typing import List, Optional
import bcrypt
from entidades.usuario_morador import Morador
from entidades.usuario_visitante import UsuarioVisitante
from interfaces.dtos.models import MoradorModel
from repositorios.usuario_repositorio import UsuarioRepositorio
from infraestrutura.connectors.sqlite_connector import SQLiteConnector


class SQLiteUsuarioRepositorio(UsuarioRepositorio):
    def __init__(self, connector: SQLiteConnector):
        self.connector = connector
        self.connector.create_tables()

    def adicionar_morador(self, morador: Morador):
        query = "INSERT INTO moradores (nome, email, telefone, cpf, data_nascimento, senha, numero_apartamento) VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = (morador.nome, morador.email, morador.telefone, morador.cpf, morador.data_nascimento, morador.senha, morador.numero_apartamento)
        self.connector.execute(query, params)
        morador.id = self.connector.cursor.lastrowid
    
    def buscar_morador_por_email(self, email):
        query = "SELECT * FROM moradores WHERE email = ?"
        self.connector.execute(query, (email,))
        result = self.connector.fetchone()
        if result:
            # Converta o resultado da consulta para um dicionário
            keys = ["id", "nome", "email", "telefone", "cpf", "data_nascimento", "senha"]
            morador_dict = dict(zip(keys, result))
            return MoradorModel(**morador_dict)
        return None

    def obter_moradores(self):
        query = "SELECT id, nome, email, telefone, cpf, data_nascimento, senha, numero_apartamento FROM moradores"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [Morador(id=row[0], nome=row[1], email=row[2], telefone=row[3], cpf=row[4], data_nascimento=row[5], senha=row[6], numero_apartamento=row[7]) for row in rows]
    
    def obter_morador_por_cpf(self, cpf: str) -> Morador:
        query = "SELECT id, nome, email, telefone, cpf, data_nascimento, senha, numero_apartamento FROM moradores WHERE cpf = ?"
        self.connector.execute(query, (cpf,))
        row = self.connector.fetchone()
        if row:
            return Morador(id=row[0], nome=row[1], email=row[2], telefone=row[3], cpf=row[4], data_nascimento=row[5], senha=row[6], numero_apartamento=row[7])
        else:
            raise ValueError("Morador não encontrado")
        
    def deletar_morador_por_cpf(self, cpf: str):
        query = "DELETE FROM moradores WHERE cpf = ?"
        self.connector.execute(query, (cpf,))
        
    def pesquisar_moradores(self, nome: Optional[str], email: Optional[str], cpf: Optional[str], data_nascimento: Optional[str]) -> List[Morador]:
        query = "SELECT id, nome, email, telefone, cpf, data_nascimento, senha FROM moradores WHERE 1=1"
        params = []
        if nome:
            query += " AND nome LIKE ?"
            params.append(f"%{nome}%")
        if email:
            query += " AND email LIKE ?"
            params.append(f"%{email}%")
        if cpf:
            query += " AND cpf = ?"
            params.append(cpf)
        if data_nascimento:
            query += " AND data_nascimento = ?"
            params.append(data_nascimento)
        
        self.connector.execute(query, tuple(params))
        rows = self.connector.fetchall()
        return [Morador(id=row[0], nome=row[1], email=row[2], telefone=row[3], cpf=row[4], data_nascimento=row[5], senha=row[6]) for row in rows]
        
    def obter_morador_por_id(self, id: int) -> Morador:
        query = "SELECT id, nome, email, telefone, cpf, data_nascimento, senha FROM moradores WHERE id = ?"
        self.connector.execute(query, (id,))
        row = self.connector.fetchone()
        if row:
            return Morador(id=row[0], nome=row[1], email=row[2], telefone=row[3], cpf=row[4], data_nascimento=row[5], senha=row[6])
        else:
            raise ValueError("Morador não encontrado")
    
    def adicionar_visitante(self, visitante: UsuarioVisitante):
        query = "INSERT INTO visitantes (nome, cpf, telefone, veiculo, data_entrada, data_saida) VALUES (?, ?, ?, ?, ?, ?)"
        params = (visitante.nome, visitante.cpf, visitante.telefone, visitante.veiculo, visitante.data_entrada, visitante.data_saida)
        self.connector.execute(query, params)

    def obter_visitantes(self):
        query = "SELECT nome, cpf, telefone, veiculo, data_entrada, data_saida FROM visitantes"
        self.connector.execute(query)
        rows = self.connector.fetchall()
        return [UsuarioVisitante(*row) for row in rows]