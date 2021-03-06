from datetime import date


class RepositorioCompra:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def crear(self, id_proveedor, id_forma_pago):
        agregar_compra = ("INSERT INTO compras "
                          "(fecha, id_proveedor, id_forma_pago) "
                          "VALUES (%s, %s, %s)")
        datos_compra = (
            date.today(), id_proveedor, id_forma_pago)
        self.cursor.execute(agregar_compra, datos_compra)
        self.cnx.commit()
        return self.cursor.lastrowid

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM compras")
        return self.cursor.fetchall()

    def buscar_por_proveedor(self, id_proveedor):
        self.cursor.execute("SELECT * FROM compras WHERE id_proveedor LIKE %s", (id_proveedor,))
        return self.cursor.fetchall()

    def buscar_por_fecha(self, fecha):
        self.cursor.execute("SELECT * FROM compras WHERE fecha LIKE %s", (fecha,))
        return self.cursor.fetchall()
