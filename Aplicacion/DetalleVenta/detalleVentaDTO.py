class DetalleVentaDTO:
    def __init__(self, venta_detalle_id, cantidad, precio, producto, total_item) -> None:
        self.id = venta_detalle_id
        self.cantidad = cantidad
        self.precio = precio
        self.producto = producto
        self.total_item = total_item
