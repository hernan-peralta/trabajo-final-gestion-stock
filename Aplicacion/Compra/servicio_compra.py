from Aplicacion.Compra.compraDTO import CompraDTO


class ServicioCompra:
    def __init__(self, repositorio_compra, repositorio_forma_pago, repositorio_proveedor, repositorio_detalle_compra):
        self.repositorioCompra = repositorio_compra
        self.repositorioFormaPago = repositorio_forma_pago
        self.repositorioProveedor = repositorio_proveedor
        self.repositorioDetalleCompra = repositorio_detalle_compra

    def obtener_todos(self):
        lista_compras = []
        lista_query = self.repositorioCompra.obtener_todos()
        for (q) in lista_query:
            total_compra = 0
            lista_detalle_compras = self.repositorioDetalleCompra.obtener_por_compra_id(q[0])
            for detalle in lista_detalle_compras:
                cantidad = detalle[1]
                precio_compra = detalle[2]
                total_compra += cantidad * precio_compra
            forma_pago = self.repositorioFormaPago.obtener_por_id(q[3])
            proveedor = self.repositorioProveedor.buscar_por_id(q[2])
            lista_compras.append(CompraDTO(q[0], q[1], forma_pago[1], total_compra, proveedor[0]))
        return lista_compras

    def buscar_por_proveedor(self):
        pass

    def buscar_por_fecha(self):
        pass
