from Aplicacion.Localidad.localidad_dto import LocalidadDTO
from Dominio.localidad import Localidad


class ServicioLocalidad:
    def __init__(self, repositorio_localidad, repositorio_provincia):
        self.repositorio_localidad = repositorio_localidad
        self.repositorio_provincia = repositorio_provincia

    def buscar_por_id(self, id_localidad):
        pass

    def buscar_por_nombre(self, nombre_localidad):
        resultado_query_localidad = self.repositorio_localidad.buscar_por_nombre(nombre_localidad)
        # resultado_query_provincia = self.repositorio_provincia.buscar_por_nombre(nombre_provincia)
        return LocalidadDTO(resultado_query_localidad[0], resultado_query_localidad[1], resultado_query_localidad[2])

    def guardar(self, localidad_request):
        id_provincia = self.repositorio_provincia.buscar_por_nombre(localidad_request["provincia"])
        localidad = Localidad(localidad_request["nombre"], localidad_request["codigo_postal"], id_provincia)
        self.repositorio_localidad.guardar(localidad)
