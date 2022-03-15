class RepositorioLocalidad:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, localidad):
        agregar_localidad = ("INSERT INTO localidades "
                             "(nombre, codigo_postal, id_provincia) "
                             "VALUES (%s, %s, %s)")
        datos_localidad = (localidad.nombre, localidad.codigo_postal, localidad.id_provincia)
        self.cursor.execute(agregar_localidad, datos_localidad)
        self.cnx.commit()

    def obtener_todos(self):
        self.cursor.execute(
            "SELECT localidades.id, localidades.nombre, localidades.codigo_postal, p.nombre FROM localidades JOIN provincias AS p ON localidades.id_provincia = p.id")
        return self.cursor.fetchall()

    def buscar_por_id(self, id_localidad):
        self.cursor.execute("SELECT * FROM localidades WHERE id LIKE %s", (id_localidad,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM localidades WHERE nombre LIKE %s", (nombre,))
        return self.cursor.fetchall()

    def buscar_por_provincia(self, nombre_provincia):
        self.cursor.execute(
            "SELECT localidades.id, localidades.nombre, localidades.codigo_postal, p.nombre FROM localidades JOIN provincias AS p ON localidades.id_provincia = p.id WHERE p.nombre = %s",
            (nombre_provincia,))
        return self.cursor.fetchall()

    def actualizar(self, localidad, localidad_id):
        actualizar_localidad = ("UPDATE localidades "
                                "SET nombre = %s, codigo_postal = %s, id_provincia = %s "
                                "WHERE id = %s")
        datos_localidad = (localidad.nombre, localidad.codigo_postal, localidad.id_provincia, localidad_id)
        self.cursor.execute(actualizar_localidad, datos_localidad)
        self.cnx.commit()

    def eliminar(self, id_localidad):
        self.cursor.execute("DELETE FROM localidades WHERE id = %s", (id_localidad,))
        self.cnx.commit()
