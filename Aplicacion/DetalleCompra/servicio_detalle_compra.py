from Aplicacion.DetalleCompra.detalleCompraDTO import DetalleCompraDTO
from Dominio.detalle_compra import DetalleCompra
from Dominio.producto import Producto


class ServicioDetalleCompra:
    def __init__(self, repositorio_detalle_compra, repositorio_producto, repositorio_compra, repositorio_proveedor,
                 repositorio_forma_pago):
        self.repositorio_forma_pago = repositorio_forma_pago
        self.repositorio_proveedor = repositorio_proveedor
        self.repositorio_compra = repositorio_compra
        self.repositorio_detalle_compra = repositorio_detalle_compra
        self.repositorio_producto = repositorio_producto

    def guardar(self, detalle_compra_request):
        proveedor = self.repositorio_proveedor.buscar_por_id(detalle_compra_request["proveedor"])
        forma_pago = self.repositorio_forma_pago.buscar_por_nombre(detalle_compra_request["forma_pago"])
        compra_id = self.repositorio_compra.crear(proveedor[0], forma_pago[0])
        for item in detalle_compra_request["lista"]:
            query_producto = self.repositorio_producto.buscar_por_nombre(item["producto"])
            producto = Producto(query_producto[0][1], query_producto[0][2], query_producto[0][3], query_producto[0][4],
                                query_producto[0][5], query_producto[0][6])
            detalle_compra = DetalleCompra(query_producto[0][0], item["precio"], item["cantidad"], compra_id)
            if producto.unidades_stock > 0:
                self.repositorio_detalle_compra.guardar(detalle_compra)
                producto.unidades_stock += int(detalle_compra.cantidad)
                self.repositorio_producto.actualizar(producto, query_producto[0][0])

    def obtener_por_compra_id(self, compra_id):
        lista_detalle_compras = []
        resultado_query = self.repositorio_detalle_compra.obtener_por_compra_id(compra_id)
        for (q) in resultado_query:
            producto = self.repositorio_producto.obtener(q[4])
            precio_detalle_compra = q[2]
            cantidad = q[1]
            total_item = precio_detalle_compra * cantidad
            lista_detalle_compras.append(DetalleCompraDTO(q[0], q[1], q[2], producto[1], total_item))
        return lista_detalle_compras
