class CompraDTO:
    def __init__(self, compra_id, fecha, forma_pago, total_compra, proveedor) -> None:
        self.id = compra_id
        self.fecha = fecha
        self.forma_pago = forma_pago
        self.total_compra = total_compra
        self.proveedor = proveedor
