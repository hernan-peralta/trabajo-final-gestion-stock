class CategoriaDTO:
    def __init__(self, categoria_id, nombre, observaciones) -> None:
        self.id = categoria_id
        self.nombre = nombre
        self.marca = observaciones
