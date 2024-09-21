from src.core.entities.users.interfaces.user_interface import UserInterface

class Morador(UserInterface):    
    def __init__(self, name: str, cpf: str, apartment_num: str, email:str, contact_num: str):   
        self._name = name
        self._cpf = cpf
        self._apartment_num = apartment_num
        self._email = email
        self._contact_num = contact_num
        
    def get_user_name(self) -> str:
        return self._name