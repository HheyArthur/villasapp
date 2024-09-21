from src.core.entities.users.interfaces.user_interface import UserInterface

class Morador(UserInterface):    
    def __init__(self, name: str, cpf: str, apartment_num: str, email:str, contact_num: str):   
        self.name = name
        self.cpf = cpf
        self.apartment_num = apartment_num
        self.email = email
        self.contact_num = contact_num