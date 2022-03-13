from Aplicacion.Venta.ventaDTO import VentaDTO


class ServicioVenta:
    def __init__(self, repositorio_venta, repositorio_forma_pago, repositorio_cliente, repositorio_detalle_venta):
        self.repositorioVenta = repositorio_venta
        self.repositorioFormaPago = repositorio_forma_pago
        self.repositorioCliente = repositorio_cliente
        self.repositorioDetalleVenta = repositorio_detalle_venta

    def obtener_todos(self):
        lista_ventas = []
        lista_query = self.repositorioVenta.obtener_todos()
        for (q) in lista_query:
            total_venta = 0
            lista_detalle_ventas = self.repositorioDetalleVenta.obtener_por_venta_id(q[0])
            for detalle in lista_detalle_ventas:
                total_venta += detalle[2]
            forma_pago = self.repositorioFormaPago.obtener_por_id(q[3])
            cliente = self.repositorioCliente.buscar_por_id(q[2])
            lista_ventas.append(VentaDTO(q[0], q[1], forma_pago[1], total_venta, cliente[0]))
        return lista_ventas

    def buscar_por_cliente(self):
        pass

    def buscar_por_fecha(self):
        pass
