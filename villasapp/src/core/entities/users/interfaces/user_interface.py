from abc import ABC, abstractmethod
from src.core.entities.users.user_morador import Morador

class UserInterface(ABC):
    @abstractmethod
    def get_user(self, user_id: int):
        raise "Unnimplemented method"