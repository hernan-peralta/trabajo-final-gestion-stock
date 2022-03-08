class ServicioProvincia:
    def __init__(self, repositorio_provincia):
        self.repositorio_provincia = repositorio_provincia

    def buscar_por_id(self, id_provincia):
        resultado_query = self.repositorio_provincia(id_provincia)
        return

    def buscar_por_nombre(self, nombre_provincia):
        resultado_query = self.repositorio_provincia.obtener_por_nombre(nombre_provincia)

