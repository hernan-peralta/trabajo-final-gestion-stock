from Aplicacion.Venta.ventaDTO import VentaDTO


class ServicioVenta:
    def __init__(self, repositorioVenta, repositorioFormaPago, repositorioCliente, repositorioDetalleVenta):
        self.repositorioVenta = repositorioVenta
        self.repositorioFormaPago = repositorioFormaPago
        self.repositorioCliente = repositorioCliente
        self.repositorioDetalleVenta = repositorioDetalleVenta

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
