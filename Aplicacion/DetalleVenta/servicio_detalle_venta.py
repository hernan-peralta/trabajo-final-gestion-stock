from Dominio.detalle_venta import DetalleVenta
from Dominio.producto import Producto


class ServicioDetalleVenta:
    def __init__(self, repositorio_detalle_venta, repositorio_producto, repositorio_venta, repositorio_cliente,
                 repositorio_forma_pago):
        self.repositorio_forma_pago = repositorio_forma_pago
        self.repositorio_cliente = repositorio_cliente
        self.repositorio_venta = repositorio_venta
        self.repositorio_detalle_venta = repositorio_detalle_venta
        self.repositorio_producto = repositorio_producto

    def guardar(self, detalle_venta_request):
        cliente = self.repositorio_cliente.buscar_por_id(detalle_venta_request["cliente"])
        forma_pago = self.repositorio_forma_pago.buscar_por_nombre(detalle_venta_request["forma_pago"])
        venta_id = self.repositorio_venta.crear(cliente[0], forma_pago[0])
        for item in detalle_venta_request["lista"]:
            query_producto = self.repositorio_producto.buscar_por_nombre(item["producto"])
            producto = Producto(query_producto[0][1], query_producto[0][2], query_producto[0][3], query_producto[0][4],
                                query_producto[0][5], query_producto[0][6])
            detalle_venta = DetalleVenta(query_producto[0][0], item["precio"], item["cantidad"], venta_id)
            if producto.unidades_stock > 0:
                self.repositorio_detalle_venta.guardar(detalle_venta)
                producto.unidades_stock -= int(detalle_venta.cantidad)
                self.repositorio_producto.actualizar(producto, query_producto[0][0])
