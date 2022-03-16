from Dominio.detalle_venta import DetalleVenta

class RepositorioDetalleVenta:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = cnx.cursor()

    def guardar(self, detalle_venta):
        agregar_detalle_venta = ("INSERT INTO detalle_venta "
                             "(cantidad, precio, id_venta, id_producto) "
                             "VALUES (%s, %s, %s, %s)")
        datos_detalle_venta = (
            detalle_venta.cantidad, detalle_venta.precio, detalle_venta.id_venta, detalle_venta.id_producto)
        self.cursor.execute(agregar_detalle_venta, datos_detalle_venta)
        self.cnx.commit()

    def obtener_por_venta_id(self, venta_id):
        self.cursor.execute("SELECT * FROM detalle_venta WHERE id_venta = %s", (venta_id,))
        detalle_ventas = []
        for atributo in self.cursor.fetchall():
            detalle_ventas.append(DetalleVenta(atributo[0], atributo[1], atributo[2], atributo[3]))
        return detalle_ventas
