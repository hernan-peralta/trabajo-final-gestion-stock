class ClienteDTO:
    def __init__(self, cliente_id, nombre, apellido, direccion, localidad, telefono, email, dni, observaciones) -> None:
        self.id = cliente_id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.localidad = localidad
        self.telefono = telefono
        self.email = email
        self.dni = dni
        self.observaciones = observaciones

