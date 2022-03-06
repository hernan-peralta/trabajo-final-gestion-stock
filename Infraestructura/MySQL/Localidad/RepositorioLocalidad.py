class RepositorioLocalidad:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, localidad):
        agregar_localidad = ("INSERT INTO localidades "
                             "(nombre, codigo_postal, id_provincia) "
                             "VALUES (%s, %s, %s)")
        datos_localidad = (localidad.nombre, localidad.observaciones, localidad.id_provincia)
        self.cursor.execute(agregar_localidad, datos_localidad)
        self.cnx.commit()

    def buscar_por_id(self, id_localidad):
        self.cursor.execute("SELECT * FROM localidades WHERE id LIKE %s", (id_localidad,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM localidades WHERE nombre LIKE %s", (nombre,))
        return self.cursor.fetchone()
