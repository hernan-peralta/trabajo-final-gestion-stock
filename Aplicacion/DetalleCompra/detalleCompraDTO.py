class DetalleCompraDTO:
    def __init__(self, compra_detalle_id, cantidad, precio, producto, total_item) -> None:
        self.id = compra_detalle_id
        self.cantidad = cantidad
        self.precio = precio
        self.producto = producto
        self.total_item = total_item
