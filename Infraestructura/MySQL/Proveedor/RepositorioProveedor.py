class RepositorioProveedor:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, proveedor):
        agregar_proveedor = ("INSERT INTO proveedores "
                             "(nombre, direccion_comercial, id_localidad, telefono, email, dni, cbu, banco_cbu, cuit, categoria_iva, observaciones) "
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        datos_proveedor = (
            proveedor.nombre, proveedor.direccion_comercial, proveedor.id_localidad, proveedor.telefono,
            proveedor.email,
            proveedor.dni, proveedor.cbu, proveedor.banco_cbu, proveedor.cuit, proveedor.categoria_iva,
            proveedor.observaciones)
        self.cursor.execute(agregar_proveedor, datos_proveedor)
        self.cnx.commit()

    def obtener_todos(self):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.banco_cbu, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id")
        return self.cursor.fetchall()

    def buscar_por_nombre(self, nombre_proveedor):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.banco_cbu, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE proveedores.nombre LIKE %s",
            (nombre_proveedor.title(),))
        return self.cursor.fetchall()

    def buscar_por_localidad(self, localidad):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.banco_cbu, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE l.nombre LIKE %s",
            (localidad.title(),))
        return self.cursor.fetchall()

    def buscar_por_provincia(self, provincia):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.banco_cbu, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN provincias AS p ON l.id_provincia = p.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE p.nombre LIKE %s",
            (provincia.title(),))
        return self.cursor.fetchall()

    def eliminar(self, id_proveedor):
        self.cursor.execute("DELETE FROM proveedores WHERE id = %s", (id_proveedor,))
        self.cnx.commit()
