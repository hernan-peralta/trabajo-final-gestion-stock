class RepositorioProvincia:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def obtener_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM provincias WHERE nombre LIKE %s", (nombre,))
        return self.cursor.fetchone()

    def obtener_por_id(self, id_provincia):
        self.cursor.execute("SELECT * FROM provincias WHERE id LIKE %s", (id_provincia,))
        return self.cursor.fetchone()
