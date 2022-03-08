from Aplicacion.Banco.banco_dto import BancoDTO
from Dominio.Banco import Banco


class ServicioBanco:
    def __init__(self, repositorio_banco):
        self.repositorio_banco = repositorio_banco

    def obtener_todos(self):
        lista_bancos = []
        lista_query = self.repositorio_banco.obtener_todos()
        for (q) in lista_query:
            lista_bancos.append(
                BancoDTO(q[0], q[1], q[2]))
        return lista_bancos

    def buscar_por_id(self, id_banco):
        pass

    def buscar_por_nombre(self, nombre_banco):
        resultado_query_banco = self.repositorio_banco.buscar_por_nombre(nombre_banco)
        return BancoDTO(resultado_query_banco[0], resultado_query_banco[1], resultado_query_banco[2])

    def guardar(self, banco_request):
        banco = Banco(banco_request["nombre"], banco_request["observaciones"])
        self.repositorio_banco.guardar(banco)
