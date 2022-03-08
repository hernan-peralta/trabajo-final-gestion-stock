from Aplicacion.Cliente.cliente_dto import ClienteDTO
from Dominio.cliente import Cliente


class ServicioCliente:
    def __init__(self, repositorio_cliente, repositorio_localidad):
        self.repositorioCliente = repositorio_cliente
        self.repositorioLocalidad = repositorio_localidad

    def guardar(self, cliente_request):
        localidad = self.repositorioLocalidad.buscar_por_nombre(cliente_request["localidad"])
        cliente = Cliente(cliente_request["nombre"], cliente_request["apellido"], cliente_request["direccion"],
                          cliente_request["localidad"], cliente_request["telefono"], cliente_request["dni"],
                          cliente_request["observaciones"])
        return self.repositorioCliente.guardar(cliente, localidad[0])

    def obtener_todos(self):
        lista_clientes = []
        lista_query = self.repositorioCliente.obtener_todos()
        for (q) in lista_query:
            lista_clientes.append(ClienteDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7]))
        return lista_clientes

    def buscar_por_id(self, id_cliente):
        resultado_query = self.repositorioCliente.buscar_por_id(id_cliente)
        return ClienteDTO(resultado_query[0], resultado_query[1], resultado_query[2], resultado_query[3],
                          resultado_query[4], resultado_query[5], resultado_query[6], resultado_query[7])

    def actualizar(self, cliente_request):
        id_cliente = int(cliente_request["id"])
        localidad = self.repositorioLocalidad.buscar_por_nombre(cliente_request["localidad"])
        cliente = Cliente(cliente_request["nombre"], cliente_request["apellido"], cliente_request["direccion"],
                          localidad[0], cliente_request["telefono"], cliente_request["dni"],
                          cliente_request["observaciones"])
        return self.repositorioCliente.actualizar(cliente, id_cliente)

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

    def eliminar(self, id_cliente):
        return self.repositorioCliente.eliminar(id_cliente)
