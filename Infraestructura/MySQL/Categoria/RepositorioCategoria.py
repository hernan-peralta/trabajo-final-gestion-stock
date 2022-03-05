class RepositorioCategoria:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, categoria):
        agregar_categoria = ("INSERT INTO categorias "
                             "(nombre, observaciones) "
                             "VALUES (%s, %s)")
        datos_categoria = (categoria.nombre, categoria.observaciones)
        self.cursor.execute(agregar_categoria, datos_categoria)
        self.cnx.commit()

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM categorias")
        return self.cursor.fetchall()

    def buscar_por_id(self, id_categoria):
        self.cursor.execute("SELECT * FROM categorias WHERE id LIKE %s", (id_categoria,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre_categoria):
        self.cursor.execute("SELECT * FROM categorias WHERE nombre LIKE %s", (nombre_categoria,))
        return self.cursor.fetchall()

    def eliminar(self, id_categoria):
        self.cursor.execute("DELETE FROM categorias WHERE id = %s", (id_categoria,))
        self.cnx.commit()
