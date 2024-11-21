class Morador:
    def __init__(self, nome, email, telefone, cpf, data_nascimento, senha, numero_apartamento=None, id=None):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__senha = senha
        self.__numero_apartamento = numero_apartamento

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self.__data_nascimento = value

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        self.__senha = value
    
    @property
    def numero_apartamento(self):
        return self.__numero_apartamento

    @numero_apartamento.setter
    def numero_apartamento(self, value):
        self.__numero_apartamento = value