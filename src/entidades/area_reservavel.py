class AreaReservavel:
    def __init__(self, disponivel: bool, nome_area: str, horario_funcionamento: str, reservado_por: str = None, data_reserva: str = None, id: int = None):
        self.__id = id
        self.__disponivel = disponivel
        self.__nome_area = nome_area
        self.__horario_funcionamento = horario_funcionamento
        self.__reservado_por = reservado_por
        self.__data_reserva = data_reserva

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, value):
        self.__disponivel = value

    @property
    def nome_area(self):
        return self.__nome_area

    @nome_area.setter
    def nome_area(self, value):
        self.__nome_area = value

    @property
    def horario_funcionamento(self):
        return self.__horario_funcionamento

    @horario_funcionamento.setter
    def horario_funcionamento(self, value):
        self.__horario_funcionamento = value

    @property
    def reservado_por(self):
        return self.__reservado_por

    @reservado_por.setter
    def reservado_por(self, value):
        self.__reservado_por = value

    @property
    def data_reserva(self):
        return self.__data_reserva

    @data_reserva.setter
    def data_reserva(self, value):
        self.__data_reserva = value