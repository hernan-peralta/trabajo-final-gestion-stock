from Aplicacion.Localidad.localidad_dto import LocalidadDTO
from Dominio.localidad import Localidad


class ServicioLocalidad:
    def __init__(self, repositorio_localidad, repositorio_provincia):
        self.repositorio_localidad = repositorio_localidad
        self.repositorio_provincia = repositorio_provincia

    def obtener_todas(self):
        lista_localidades = []
        lista_query = self.repositorio_localidad.obtener_todos()
        for (q) in lista_query:
            lista_localidades.append(
                LocalidadDTO(q[0], q[1], q[2], q[3]))
        return lista_localidades

    def buscar_por_id(self, id_localidad):
        resultado_query_localidad = self.repositorio_localidad.buscar_por_id(id_localidad)
        resultado_query_provincia = self.repositorio_provincia.obtener_por_id(resultado_query_localidad[3])
        return LocalidadDTO(resultado_query_localidad[0], resultado_query_localidad[1], resultado_query_localidad[2],
                            resultado_query_provincia[1])

    def buscar_por_nombre(self, nombre_localidad):
        lista_query = self.repositorio_localidad.buscar_por_nombre(nombre_localidad)
        lista_localidades = []
        for (q) in lista_query:
            resultado_query_provincia = self.repositorio_provincia.obtener_por_id(q[3])
            lista_localidades.append(
                LocalidadDTO(q[0], q[1], q[2], resultado_query_provincia[1]))
        return lista_localidades

    def buscar_por_provincia(self, nombre_provincia):
        #TODO
        pass

    def guardar(self, localidad_request):
        provincia = self.repositorio_provincia.obtener_por_nombre(localidad_request["provincia"])
        localidad = Localidad(localidad_request["nombre"], localidad_request["codigo_postal"], provincia[0])
        self.repositorio_localidad.guardar(localidad)

    def actualizar(self, localidad_request):
        id_localidad = int(localidad_request["id"])
        provincia = self.repositorio_provincia.obtener_por_nombre(localidad_request["provincia"])
        localidad = Localidad(localidad_request["nombre"], localidad_request["codigo_postal"], provincia[0])
        return self.repositorio_localidad.actualizar(localidad, id_localidad)

    def eliminar(self, id_localidad):
        return self.repositorio_localidad.eliminar(id_localidad)
