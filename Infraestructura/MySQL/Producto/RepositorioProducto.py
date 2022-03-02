class RepositorioProducto:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, producto):
        #TODO asociar la categoria
        agregar_producto = ("INSERT INTO prodçuctos "
                            "(nombre, marca, precio_unitario, unidades_stock, descripcion, observaciones) "
                            "VALUES (%s, %s, %s, %s, %s, %s)")
        datos_producto = (
            producto.nombre, producto.marca, producto.precio_unitario, producto.unidades_stock, producto.descripcion,
            producto.observaciones)
        self.cursor.execute(agregar_producto, datos_producto)
        self.cnx.commit()

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def obtener(self, id_producto):
        self.cursor.execute("SELECT * FROM productos WHERE id = %s", (id_producto,))
        return self.cursor.fetchall()

    def buscar_por_nombre(self, nombre_producto):
        self.cursor.execute("SELECT * FROM productos WHERE nombre LIKE %s", (nombre_producto,))
        return self.cursor.fetchall()

    def buscar_por_marca(self, nombre_marca):
        self.cursor.execute("SELECT * FROM productos WHERE marca LIKE %s", (nombre_marca,))
        return self.cursor.fetchall()

    def buscar_por_categoria(self, nombre_categoria):
        self.cursor.execute(
            "SELECT productos.id, productos.nombre, productos.marca, productos.precio_unitario, productos.unidades_stock, productos.descripcion, productos.observaciones FROM productos JOIN categorias_productos AS c_p ON productos.id = c_p.id_producto JOIN categorias ON categorias.id = c_p.id_categoria WHERE categorias.nombre = %s",
            (nombre_categoria,))
        return self.cursor.fetchall()

    def eliminar(self, id_producto):
        self.cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
        self.cnx.commit()
