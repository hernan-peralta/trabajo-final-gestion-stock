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

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM bancos")
        return self.cursor.fetchall()

    def buscar_por_id(self, id_banco):
        self.cursor.execute("SELECT * FROM bancos WHERE id LIKE %s", (id_banco,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM bancos WHERE nombre LIKE %s", (nombre,))
        return self.cursor.fetchone()

    def actualizar(self, banco, id_banco):
        actualizar_banco = ("UPDATE bancos "
                             "SET nombre = %s, observaciones = %s "
                             "WHERE id = %s")
        datos_banco = (banco.nombre, banco.observaciones, id_banco)
        self.cursor.execute(actualizar_banco, datos_banco)
        self.cnx.commit()

    def eliminar(self, id_banco):
        self.cursor.execute("DELETE FROM bancos WHERE id = %s", (id_banco,))
        self.cnx.commit()
