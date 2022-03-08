class RepositorioBanco:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, banco):
        agregar_banco = ("INSERT INTO bancos "
                         "(nombre, observaciones) "
                         "VALUES (%s, %s)")
        datos_banco = (banco.nombre, banco.observaciones)
        self.cursor.execute(agregar_banco, datos_banco)
        self.cnx.commit()

    def buscar_por_id(self, id_banco):
        self.cursor.execute("SELECT * FROM bancos WHERE id LIKE %s", (id_banco,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM bancos WHERE nombre LIKE %s", (nombre,))
        return self.cursor.fetchone()

    def eliminar(self, id_banco):
        self.cursor.execute("DELETE FROM bancos WHERE id = %s", (id_banco,))
        self.cnx.commit()
