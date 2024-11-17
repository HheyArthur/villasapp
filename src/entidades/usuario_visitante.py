class UsuarioVisitante:
    def __init__(self, nome, cpf, telefone, veiculo, data_entrada, data_saida):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__veiculo = veiculo
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, value):
        self.__veiculo = value

    @property
    def data_entrada(self):
        return self.__data_entrada

    @data_entrada.setter
    def data_entrada(self, value):
        self.__data_entrada = value

    @property
    def data_saida(self):
        return self.__data_saida

    @data_saida.setter
    def data_saida(self, value):
        self.__data_saida = value