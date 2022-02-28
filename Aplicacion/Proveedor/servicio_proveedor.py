from Aplicacion.Proveedor.proveedor_dto import ProveedorDTO


class ServicioProveedor:
    def __init__(self, repositorio_proveedor):
        self.repositorioProveedor = repositorio_proveedor

    def guardar(self, proveedor):
        return self.repositorioProveedor.guardar(proveedor)

    def obtener_todos(self):
        lista_proveedores = []
        lista_query = self.repositorioProveedor.obtener_todos()
        for (q) in lista_query:
            lista_proveedores.append(ProveedorDTO(q[0], q[1], q[2], q[3], q[4]))
        return lista_proveedores

    def obtener_id(self, proveedor_id):
        return self.repositorioProveedor.obtener(proveedor_id)

