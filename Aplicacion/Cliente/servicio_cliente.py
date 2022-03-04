from Aplicacion.Cliente.cliente_dto import ClienteDTO


class ServicioCliente:
    def __init__(self, repositorio_cliente):
        self.repositorioCliente = repositorio_cliente

    def guardar(self, cliente):
        return self.repositorioCliente.guardar(cliente)

    def obtener_todos(self):
        lista_clientes = []
        lista_query = self.repositorioCliente.obtener_todos()
        for (q) in lista_query:
            lista_clientes.append(ClienteDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
        return lista_clientes

    def buscar_por_nombre(self, nombre):
        lista_clientes = []
        lista_query = self.repositorioCliente.buscar_por_nombre(nombre)
        for (q) in lista_query:
            lista_clientes.append(ClienteDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
        return lista_clientes

    def buscar_por_apellido(self, apellido):
        lista_clientes = []
        lista_query = self.repositorioCliente.buscar_por_apellido(apellido)
        for (q) in lista_query:
            lista_clientes.append(ClienteDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
        return lista_clientes

    def buscar_por_localidad(self, localidad):
        lista_clientes = []
        lista_query = self.repositorioCliente.buscar_por_localidad(localidad)
        for (q) in lista_query:
            lista_clientes.append(ClienteDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
        return lista_clientes

    def buscar_por_provincia(self, provincia):
        lista_clientes = []
        lista_query = self.repositorioCliente.buscar_por_provincia(provincia)
        for (q) in lista_query:
            lista_clientes.append(ClienteDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
        return lista_clientes
