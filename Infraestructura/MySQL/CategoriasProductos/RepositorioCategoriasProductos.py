class RepositorioCategoriasProductos:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, id_producto, id_categoria):
        agregar_categorias_productos = ("INSERT INTO categorias_productos "
                             "(id_producto, id_categoria) "
                             "VALUES (%s, %s)")
        datos_categorias_productos = (id_producto, id_categoria)
        self.cursor.execute(agregar_categorias_productos, datos_categorias_productos)
        self.cnx.commit()
