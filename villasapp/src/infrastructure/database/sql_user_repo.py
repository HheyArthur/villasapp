import sqlite3
from src.core.repositories.user_repository import UserRepository
from src.core.entities.users.user_morador import Morador
from src.core.entities.users.user_colaborador import Colaborador
from src.core.entities.users.user_visitante import Visitante

class SQLiteUserRepository(UserRepository):
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        
    def add_user(self, user: Morador) -> Morador:
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO morador (name, cpf, apartment_num, email, contact_num) VALUES (?, ?, ?, ?, ?)", (user.get_user_name(), user.get_user_cpf(), user.get_user_apartment_num(), user.get_user_email(), user.get_user_contact_num()))
        self.connection.commit()
        user.id = cursor.lastrowid
        return user
    
    def get(self, user_id: int) -> Morador:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM morador WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            return Morador(row[1], row[2], row[3], row[4], row[5])
        return None
