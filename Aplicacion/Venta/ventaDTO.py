class VentaDTO:
    def __init__(self, venta_id, fecha, forma_pago, total_venta, cliente) -> None:
        self.id = venta_id
        self.fecha = fecha
        self.forma_pago = forma_pago
        self.total_venta = total_venta
        self.cliente = cliente
