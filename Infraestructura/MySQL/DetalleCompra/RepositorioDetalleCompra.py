class RepositorioDetalleCompra:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, detalle_compra):
        agregar_detalle_compra = ("INSERT INTO detalle_compra "
                             "(cantidad, precio, id_compra, id_producto) "
                             "VALUES (%s, %s, %s, %s)")
        datos_detalle_compra = (
            detalle_compra.cantidad, detalle_compra.precio, detalle_compra.id_compra, detalle_compra.id_producto)
        self.cursor.execute(agregar_detalle_compra, datos_detalle_compra)
        self.cnx.commit()

    def obtener_por_compra_id(self, compra_id):
        self.cursor.execute("SELECT * FROM detalle_compra WHERE id_compra = %s", (compra_id,))
        return self.cursor.fetchall()
