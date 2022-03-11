from Aplicacion.Proveedor.proveedor_dto import ProveedorDTO
from Dominio.proveedor import Proveedor


class ServicioProveedor:
    def __init__(self, repositorio_proveedor, repositorio_banco, repositorio_localidad, repositorio_categoria_iva):
        self.repositorio_categoria_iva = repositorio_categoria_iva
        self.repositorio_localidad = repositorio_localidad
        self.repositorioProveedor = repositorio_proveedor
        self.repositorio_banco = repositorio_banco

    def guardar(self, proveedor_request):
        banco = self.repositorio_banco.buscar_por_nombre(proveedor_request["banco_cbu"])
        localidad = self.repositorio_localidad.buscar_por_nombre(proveedor_request["localidad"])
        categoria_iva = self.repositorio_categoria_iva.buscar_por_nombre(proveedor_request["categoria_iva"])
        proveedor = Proveedor(proveedor_request["nombre"], proveedor_request["direccion_comercial"],
                              localidad[0][0], proveedor_request["telefono"],
                              proveedor_request["email"], proveedor_request["dni"], proveedor_request["cbu"],
                              banco[0][0],
                              proveedor_request["cuit"], categoria_iva[0][0],
                              proveedor_request["observaciones"])
        return self.repositorioProveedor.guardar(proveedor)

    def obtener_todos(self):
        lista_proveedores = []
        lista_query = self.repositorioProveedor.obtener_todos()
        for (q) in lista_query:
            banco = self.repositorio_banco.buscar_por_id(q[8])
            lista_proveedores.append(
                ProveedorDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], banco[1], q[9], q[10], q[11]))
        return lista_proveedores

    def buscar_por_id(self, id_proveedor):
        resultado_query = self.repositorioProveedor.buscar_por_id(id_proveedor)
        return ProveedorDTO(resultado_query[0], resultado_query[1], resultado_query[2], resultado_query[3],
                            resultado_query[4], resultado_query[5], resultado_query[6], resultado_query[7],
                            resultado_query[8], resultado_query[9], resultado_query[10], resultado_query[11])

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
