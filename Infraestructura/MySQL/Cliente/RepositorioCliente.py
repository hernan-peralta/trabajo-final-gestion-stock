class RepositorioCliente:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, cliente):
        agregar_cliente = ("INSERT INTO clientes "
                           "(nombre, apellido, direccion, id_localidad, telefono, email, dni, observaciones) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        datos_cliente = (cliente.nombre, cliente.apellido, cliente.id_localidad, cliente.telefono, cliente.email,
                         cliente.dni, cliente.observaciones)
        self.cursor.execute(agregar_cliente, datos_cliente)
        self.cnx.commit()

    def obtener_todos(self):
        self.cursor.execute(
            "SELECT clientes.id, clientes.nombre, clientes.apellido, clientes.direccion, l.nombre, clientes.telefono, clientes.dni, clientes.observaciones FROM clientes JOIN localidades AS l ON clientes.id_localidad = l.id")
        return self.cursor.fetchall()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute(
            "SELECT clientes.id, clientes.nombre, clientes.apellido, clientes.direccion, l.nombre, clientes.telefono, clientes.dni, clientes.observaciones FROM clientes JOIN localidades AS l ON clientes.id_localidad = l.id WHERE clientes.nombre LIKE %s",
            (nombre.title(),))
        return self.cursor.fetchall()

    def buscar_por_apellido(self, apellido):
        self.cursor.execute(
            "SELECT clientes.id, clientes.nombre, clientes.apellido, clientes.direccion, l.nombre, clientes.telefono, clientes.dni, clientes.observaciones FROM clientes JOIN localidades AS l ON clientes.id_localidad = l.id WHERE apellido LIKE %s",
            (apellido,))
        return self.cursor.fetchall()

    def buscar_por_localidad(self, localidad):
        self.cursor.execute(
            "SELECT clientes.id, clientes.nombre, clientes.apellido, clientes.direccion, l.nombre, clientes.telefono, clientes.dni, clientes.observaciones FROM clientes JOIN localidades AS l ON clientes.id_localidad = l.id WHERE l.nombre LIKE %s",
            (localidad,))
        return self.cursor.fetchall()

    def buscar_por_provincia(self, provincia):
        self.cursor.execute(
            "SELECT clientes.id, clientes.nombre, clientes.apellido, clientes.direccion, l.nombre, clientes.telefono, clientes.dni, clientes.observaciones FROM clientes JOIN localidades as l ON clientes.id_localidad = l.id JOIN provincias as p ON l.id_provincia = p.id WHERE p.nombre LIKE %s",
            (provincia,))
        return self.cursor.fetchall()
