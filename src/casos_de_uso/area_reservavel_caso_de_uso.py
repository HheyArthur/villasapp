from entidades.area_reservavel import AreaReservavel
from repositorios.area_reservavel_repositorio import AreaReservavelRepositorio

class AreaReservavelCasosDeUso:
    def __init__(self, repositorio: AreaReservavelRepositorio):
        self.repositorio = repositorio

    def adicionar_area_reservavel(self, disponivel: bool, nome_area: str, horario_funcionamento: str, reservado_por: str = None):
        area_reservavel = AreaReservavel(disponivel=disponivel, nome_area=nome_area, horario_funcionamento=horario_funcionamento, reservado_por=reservado_por)
        self.repositorio.adicionar_area_reservavel(area_reservavel)
    
    def obter_areas_reservaveis(self):
        return self.repositorio.obter_areas_reservaveis()
    
    def obter_area_reservavel_por_nome(self, nome: str) -> AreaReservavel:
        return self.repositorio.obter_area_reservavel_por_nome(nome)
    
    def obter_area_reservavel_por_nome_aproximado(self, nome: str) -> AreaReservavel:
        return self.repositorio.obter_area_reservavel_por_nome_aproximado(nome)
    
    def atualizar_disponibilidade_area_reservavel(self, nome_area: str, disponivel: bool):
        area_reservavel = self.repositorio.obter_area_reservavel_por_nome(nome_area)
        if area_reservavel:
            self.repositorio.atualizar_disponibilidade_area_reservavel(area_reservavel.id, disponivel)
        else:
            raise ValueError("Área reservável não encontrada")
    
    def obtendo_areas_reservaveis_por_disponibilidade(self, disponibilidade: bool):
        return self.repositorio.obtendo_areas_reservaveis_por_disponibilidade(disponibilidade)