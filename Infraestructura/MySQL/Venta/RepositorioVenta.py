from datetime import date

class RepositorioVenta:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def crear(self, id_cliente, id_forma_pago):
        agregar_venta = ("INSERT INTO ventas "
                             "(fecha, id_cliente, id_forma_pago) "
                             "VALUES (%s, %s, %s)")
        datos_venta = (
            date.today(), id_cliente, id_forma_pago)
        self.cursor.execute(agregar_venta, datos_venta)
        self.cnx.commit()
        return self.cursor.lastrowid

    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM ventas")
        return self.cursor.fetchall()

    def buscar_por_cliente(self, id_cliente):
        self.cursor.execute("SELECT * FROM ventas WHERE id_cliente LIKE %s", (id_cliente,))
        return self.cursor.fetchall()
