class Recado:
    def __init__(self, conteudo, cpf_autor, id=None):
        self.__id = id
        self.__conteudo = conteudo
        self.__cpf_autor = cpf_autor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, value):
        self.__conteudo = value

    @property
    def cpf_autor(self):
        return self.__cpf_autor

    @cpf_autor.setter
    def cpf_autor(self, value):
        self.__cpf_autor = value