class ProductoDTO:
    def __init__(self, producto_id, nombre, marca, precio_unitario, unidades_stock, descripcion, observaciones) -> None:
        self.id = producto_id
        self.nombre = nombre
        self.marca = marca
        self.precio_unitario = precio_unitario
        self.unidades_stock = unidades_stock
        self.descripcion = descripcion
        self.observaciones = observaciones

