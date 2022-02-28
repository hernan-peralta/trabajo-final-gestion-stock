class ProveedorDTO:
    def __init__(self, proveedor_id, nombre, direccion_comercial, id_localidad, telefono, email, dni, cbu, banco_cbu,
                 cuit, id_categoria_iva, observaciones) -> None:
        self.id = proveedor_id
        self.nombre = nombre
        self.direccion_comercial = direccion_comercial
        self.id_localidad = id_localidad
        self.telefono = telefono
        self.email = email
        self.dni = dni
        self.cbu = cbu
        self.banco_cbu = banco_cbu
        self.cuit = cuit
        self.id_categoria_iva = id_categoria_iva
        self.observaciones = observaciones

