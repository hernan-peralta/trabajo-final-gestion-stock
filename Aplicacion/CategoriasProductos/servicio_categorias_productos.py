class ServicioCategoriasProductos:
    def __init__(self, repositorio_categorias_productos):
        self.repositorioCategoriasProductos = repositorio_categorias_productos

    def guardar(self, id_producto, id_categoria):
        return self.repositorioCategoriasProductos.guardar(id_producto, id_categoria)
