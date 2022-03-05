from Aplicacion.Categoria.categoria_dto import CategoriaDTO
from Dominio.categoria import Categoria


class ServicioCategoria:
    def __init__(self, repositorio_categoria):
        self.repositorioCategoria = repositorio_categoria

    def guardar(self, categoria_request):
        categoria = Categoria(categoria_request["nombre"], categoria_request["observaciones"])
        return self.repositorioCategoria.guardar(categoria)

    def obtener_todas(self):
        lista_categorias = []
        lista_query = self.repositorioCategoria.obtener_todos()
        for (q) in lista_query:
            lista_categorias.append(CategoriaDTO(q[0], q[1], q[2]))
        return lista_categorias

    def buscar_por_id(self, id_categoria):
        resultado_query = self.repositorioCategoria.buscar_por_id(id_categoria)
        return CategoriaDTO(resultado_query[0], resultado_query[1], resultado_query[2])

    def buscar_por_nombre(self, nombre):
        lista_categorias = []
        resultado_query = self.repositorioCategoria.buscar_por_nombre(nombre)
        for (q) in resultado_query:
            lista_categorias.append(CategoriaDTO(q[0], q[1], q[2]))
        return lista_categorias

    def actualizar(self, categoria_request):
        id_categoria = int(categoria_request["id"])
        categoria = Categoria(categoria_request["nombre"], categoria_request["observaciones"])
        return self.repositorioCategoria.actualizar(categoria, id_categoria)

    def eliminar(self, id_categoria):
        return self.repositorioCategoria.eliminar(id_categoria)
