from Aplicacion.Producto.producto_dto import ProductoDTO
from Dominio.producto import Producto


class ServicioProducto:
    def __init__(self, repositorio_producto):
        self.repositorioProducto = repositorio_producto

    def guardar(self, producto_request):
        producto = Producto(producto_request["nombre"], producto_request["marca"], producto_request["precio_unitario"],
                            producto_request["unidades_stock"], producto_request["descripcion"],
                            producto_request["observaciones"])
        return self.repositorioProducto.guardar(producto)

    def obtener_todos(self):
        lista_productos = []
        lista_query = self.repositorioProducto.obtener_todos()
        for (q) in lista_query:
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6]))
        return lista_productos

    def obtener_id(self, producto_id):
        resultado_query = self.repositorioProducto.obtener(producto_id)
        return ProductoDTO(resultado_query[0], resultado_query[1], resultado_query[2], resultado_query[3],
                           resultado_query[4], resultado_query[5], resultado_query[6])

    def buscar_por_nombre(self, nombre):
        lista_productos = []
        lista_query = self.repositorioProducto.buscar_por_nombre(nombre)
        for (q) in lista_query:
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6]))
        return lista_productos

    def buscar_por_marca(self, marca):
        lista_productos = []
        lista_query = self.repositorioProducto.buscar_por_marca(marca)
        for (q) in lista_query:
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6]))
        return lista_productos

    def buscar_por_categoria(self, categoria):
        lista_productos = []
        lista_query = self.repositorioProducto.buscar_por_categoria(categoria)
        for (q) in lista_query:
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6]))
        return lista_productos

    def eliminar(self, id_producto):
        self.repositorioProducto.eliminar(id_producto)
