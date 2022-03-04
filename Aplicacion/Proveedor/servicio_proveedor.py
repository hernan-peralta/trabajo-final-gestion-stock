from Aplicacion.Proveedor.proveedor_dto import ProveedorDTO
from Dominio.proveedor import Proveedor


class ServicioProveedor:
    def __init__(self, repositorio_proveedor):
        self.repositorioProveedor = repositorio_proveedor

    def guardar(self, proveedor_request):
        proveedor = Proveedor(proveedor_request["nombre"], proveedor_request["direccion_comercial"],
                              proveedor_request["localidad"], proveedor_request["dni"], proveedor_request["telefono"],
                              proveedor_request["email"], proveedor_request["cbu"], proveedor_request["banco_cbu"],
                              proveedor_request["cuit"], proveedor_request["categoria_iva"], proveedor_request["observaciones"])
        return self.repositorioProveedor.guardar(proveedor)

    def obtener_todos(self):
        lista_proveedores = []
        lista_query = self.repositorioProveedor.obtener_todos()
        for (q) in lista_query:
            lista_proveedores.append(
                ProveedorDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]))
        return lista_proveedores

    def buscar_por_nombre(self, nombre):
        lista_proveedores = []
        lista_query = self.repositorioProveedor.buscar_por_nombre(nombre)
        for (q) in lista_query:
            lista_proveedores.append(
                ProveedorDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]))
        return lista_proveedores

    def buscar_por_localidad(self, localidad):
        lista_proveedores = []
        lista_query = self.repositorioProveedor.buscar_por_localidad(localidad)
        for (q) in lista_query:
            lista_proveedores.append(
                ProveedorDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]))
        return lista_proveedores

    def buscar_por_provincia(self, provincia):
        lista_proveedores = []
        lista_query = self.repositorioProveedor.buscar_por_provincia(provincia)
        for (q) in lista_query:
            lista_proveedores.append(
                ProveedorDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]))
        return lista_proveedores
