class ProveedorDTO:
    def __init__(self, proveedor_id, nombre, direccion_comercial, localidad, telefono, email, dni, cbu, banco_cbu,
                 cuit, categoria_iva, observaciones) -> None:
        self.id = proveedor_id
        self.nombre = nombre
        self.direccion_comercial = direccion_comercial
        self.localidad = localidad
        self.telefono = telefono
        self.email = email
        self.dni = dni
        self.cbu = cbu
        self.banco_cbu = banco_cbu
        self.cuit = cuit
        self.categoria_iva = categoria_iva
        self.observaciones = observaciones

