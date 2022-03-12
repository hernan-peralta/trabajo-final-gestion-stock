class RepositorioProveedor:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, proveedor):
        agregar_proveedor = ("INSERT INTO proveedores "
                             "(nombre, direccion_comercial, id_localidad, telefono, email, dni, cbu, id_banco, cuit, id_categoria_iva, observaciones) "
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        datos_proveedor = (
            proveedor.nombre, proveedor.direccion_comercial, proveedor.id_localidad, proveedor.telefono,
            proveedor.email,
            proveedor.dni, proveedor.cbu, proveedor.id_banco, proveedor.cuit, proveedor.id_categoria_iva,
            proveedor.observaciones)
        self.cursor.execute(agregar_proveedor, datos_proveedor)
        self.cnx.commit()

    def obtener_todos(self):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.id_banco, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id")
        return self.cursor.fetchall()

    def buscar_por_id(self, id_proveedor):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.id_banco, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE proveedores.id LIKE %s",
            (id_proveedor,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre_proveedor):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.id_banco, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE proveedores.nombre LIKE %s",
            (nombre_proveedor.title(),))
        return self.cursor.fetchall()

    def buscar_por_localidad(self, localidad):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.id_banco, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE l.nombre LIKE %s",
            (localidad.title(),))
        return self.cursor.fetchall()

    def buscar_por_provincia(self, provincia):
        self.cursor.execute(
            "SELECT proveedores.id, proveedores.nombre, proveedores.direccion_comercial, l.nombre, proveedores.telefono, proveedores.email, proveedores.dni, proveedores.cbu, proveedores.id_banco, proveedores.cuit, c_i.categoria_iva, proveedores.observaciones FROM proveedores JOIN localidades AS l ON proveedores.id_localidad = l.id JOIN provincias AS p ON l.id_provincia = p.id JOIN categoria_iva AS c_i on proveedores.id_categoria_iva = c_i.id WHERE p.nombre LIKE %s",
            (provincia.title(),))
        return self.cursor.fetchall()

    def actualizar(self, proveedor, proveedor_id):
        actualizar_proveedor = ("UPDATE proveedores "
                             "SET nombre = %s, direccion_comercial = %s, id_localidad = %s, telefono = %s, email = %s, dni = %s, cbu = %s, id_banco = %s, cuit = %s, id_categoria_iva = %s, observaciones = %s  "
                             "WHERE id = %s")
        datos_proveedor = (
            proveedor.nombre, proveedor.direccion_comercial, proveedor.id_localidad, proveedor.telefono,
            proveedor.email,
            proveedor.dni, proveedor.cbu, proveedor.id_banco, proveedor.cuit, proveedor.id_categoria_iva,
            proveedor.observaciones, proveedor_id)
        self.cursor.execute(actualizar_proveedor, datos_proveedor)
        self.cnx.commit()

    def eliminar(self, id_proveedor):
        self.cursor.execute("DELETE FROM proveedores WHERE id = %s", (id_proveedor,))
        self.cnx.commit()
