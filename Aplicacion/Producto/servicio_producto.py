from Aplicacion.Producto.producto_dto import ProductoDTO
from Dominio.producto import Producto


class ServicioProducto:
    def __init__(self, repositorio_producto, servicio_categoria, repositorio_categorias_productos):
        self.repositorioProducto = repositorio_producto
        self.servicio_categoria = servicio_categoria
        self.repositorio_categorias_productos = repositorio_categorias_productos


    def guardar(self, producto_request):
        producto = Producto(producto_request["nombre"], producto_request["marca"],
                            producto_request["precio_unitario"],
                            producto_request["unidades_stock"], producto_request["descripcion"],
                            producto_request["observaciones"])
        producto_id = self.repositorioProducto.guardar(producto)
        for categoria_nombre in producto_request["categoria"]:
            categoria = self.servicio_categoria.buscar_por_nombre(categoria_nombre)
            self.repositorio_categorias_productos.guardar(producto_id, categoria[0].id)

    def actualizar(self, producto_request):
        id_producto = int(producto_request["id"])
        producto = Producto(producto_request["nombre"], producto_request["marca"],
                            producto_request["precio_unitario"],
                            producto_request["unidades_stock"], producto_request["descripcion"],
                            producto_request["observaciones"])
        return self.repositorioProducto.actualizar(producto, id_producto)

    def obtener_todos(self):
        lista_productos = []
        lista_query = self.repositorioProducto.obtener_todos()
        for (q) in lista_query:
            lista_categorias = self.obtener_categorias_producto(q[0])
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], lista_categorias, q[5], q[6]))
        return lista_productos

    def buscar_por_id(self, producto_id):
        resultado_query = self.repositorioProducto.obtener(producto_id)
        lista_categorias = self.obtener_categorias_producto(producto_id)
        return ProductoDTO(resultado_query[0], resultado_query[1], resultado_query[2], resultado_query[3],
                           resultado_query[4], lista_categorias, resultado_query[5], resultado_query[6])

    def buscar_por_nombre(self, nombre):
        lista_productos = []
        lista_query = self.repositorioProducto.buscar_por_nombre(nombre)
        for (q) in lista_query:
            lista_categorias = self.obtener_categorias_producto(q[0])
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], lista_categorias, q[5], q[6]))
        return lista_productos

    def buscar_por_marca(self, marca):
        lista_productos = []
        lista_query = self.repositorioProducto.buscar_por_marca(marca)
        for (q) in lista_query:
            lista_categorias = self.obtener_categorias_producto(q[0])
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], lista_categorias, q[5], q[6]))
        return lista_productos

    def buscar_por_categoria(self, categoria):
        lista_productos = []
        lista_query = self.repositorioProducto.buscar_por_categoria(categoria)
        for (q) in lista_query:
            lista_categorias = self.obtener_categorias_producto(q[0])
            lista_productos.append(ProductoDTO(q[0], q[1], q[2], q[3], q[4], lista_categorias, q[5], q[6]))
        return lista_productos

    def eliminar(self, id_producto):
        self.repositorio_categorias_productos.eliminar(id_producto)
        self.repositorioProducto.eliminar(id_producto)

    def obtener_categorias_producto(self, id_producto):
        categorias_producto = self.repositorioProducto.obtener_categorias_producto(id_producto)
        lista_categorias = []
        for cat in categorias_producto:
            lista_categorias.append(cat[0])

        return lista_categorias
