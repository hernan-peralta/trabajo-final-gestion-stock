class DetalleVenta:
    def __init__(self, id_producto, precio, cantidad, id_venta):
        self.id_producto = id_producto
        self.precio = precio
        self.cantidad = cantidad
        self.id_venta = id_venta

    def calcular_total_item(self):
        return self.precio * self.cantidad
