import os
import atexit
from pathlib import Path
from dotenv import load_dotenv
from Aplicacion.Producto.servicio_producto import ServicioProducto
from Aplicacion.Cliente.servicio_cliente import ServicioCliente
from Aplicacion.Proveedor.servicio_proveedor import ServicioProveedor
from Aplicacion.Categoria.servicio_categoria import ServicioCategoria
from Aplicacion.Localidad.servicio_localidad import ServicioLocalidad
from Aplicacion.Banco.servicio_banco import ServicioBanco
from Aplicacion.CategoriasProductos.servicio_categorias_productos import ServicioCategoriasProductos
from Aplicacion.DetalleVenta.servicio_detalle_venta import ServicioDetalleVenta
from Infraestructura.MySQL.Producto.RepositorioProducto import RepositorioProducto
from Infraestructura.MySQL.Cliente.RepositorioCliente import RepositorioCliente
from Infraestructura.MySQL.Proveedor.RepositorioProveedor import RepositorioProveedor
from Infraestructura.MySQL.Categoria.RepositorioCategoria import RepositorioCategoria
from Infraestructura.MySQL.Localidad.RepositorioLocalidad import RepositorioLocalidad
from Infraestructura.MySQL.Provincia.RepositorioProvincia import RepositorioProvincia
from Infraestructura.MySQL.Banco.RepositorioBanco import RepositorioBanco
from Infraestructura.MySQL.CategoriasProductos.RepositorioCategoriasProductos import RepositorioCategoriasProductos
from Infraestructura.MySQL.CategoriaIva.RepositorioCategoriaIva import RepositorioCategoriaIva
from Infraestructura.MySQL.DetalleVenta.RepositorioDetalleVenta import RepositorioDetalleVenta
from Infraestructura.MySQL.Venta.RepositorioVenta import RepositorioVenta
from Infraestructura.MySQL.FormaPago.RepositorioFormaPago import RepositorioFormaPago
from Gui.aplicacion import crear_aplicacion

import mysql.connector

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")

cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_DATABASE)

cursor = cnx.cursor()

repositorioLocalidad = RepositorioLocalidad(cnx)
repositorioProvincia = RepositorioProvincia(cnx)
servicioLocalidad = ServicioLocalidad(repositorioLocalidad, repositorioProvincia)

repositorioCliente = RepositorioCliente(cnx)
servicioCliente = ServicioCliente(repositorioCliente, repositorioLocalidad)

repositorioCategoriaIva = RepositorioCategoriaIva(cnx)
repositorioBanco = RepositorioBanco(cnx)
servicioBanco = ServicioBanco(repositorioBanco)
repositorioProveedor = RepositorioProveedor(cnx)
servicioProveedor = ServicioProveedor(repositorioProveedor, repositorioBanco, repositorioLocalidad,
                                      repositorioCategoriaIva)

repositorioCategoria = RepositorioCategoria(cnx)
servicioCategoria = ServicioCategoria(repositorioCategoria)

repositorioCategoriasProductos = RepositorioCategoriasProductos(cnx)
servicioCategoriasProductos = ServicioCategoriasProductos(repositorioCategoriasProductos)

repositorioProducto = RepositorioProducto(cnx)
servicioProducto = ServicioProducto(repositorioProducto, servicioCategoria, servicioCategoriasProductos)

repositorioFormaPago = RepositorioFormaPago(cnx)
repositorioDetalleVenta = RepositorioDetalleVenta(cnx)
repositorioVenta = RepositorioVenta(cnx)
servicioDetalleVenta = ServicioDetalleVenta(repositorioDetalleVenta, repositorioProducto, repositorioVenta,
                                            repositorioCliente, repositorioFormaPago)

crear_aplicacion(servicioProducto, servicioCliente, servicioProveedor, servicioCategoria, servicioLocalidad,
                 servicioBanco, servicioDetalleVenta)

atexit.register(lambda: cursor.close(), cnx.close())
