class RepositorioCategoriaIva:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, categoria_iva):
        agregar_categoria_iva = ("INSERT INTO categoria_iva "
                                 "(categoria_iva) "
                                 "VALUES (%s)")
        datos_categoria_iva = categoria_iva
        self.cursor.execute(agregar_categoria_iva, datos_categoria_iva)
        self.cnx.commit()

    def buscar_por_nombre(self, categoria_iva):
        self.cursor.execute("SELECT * FROM categoria_iva WHERE categoria_iva LIKE %s", (categoria_iva,))
        return self.cursor.fetchall()
