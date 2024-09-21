from src.core.entities.users.interfaces.user_interface import UserInterface

class Morador(UserInterface):    
    def __init__(self, name: str, cpf: str, apartment_num: str, email:str, contact_num: str):   
        self.__name = name
        self.__cpf = cpf
        self.__apartment_num = apartment_num
        self.__email = email
        self.__contact_num = contact_num
        
    def get_user_name(self) -> str:
        return self.__name
    
    def set_user_name(self, name: str):
        self.__name = name