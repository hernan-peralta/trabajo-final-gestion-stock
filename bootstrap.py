import os
from pathlib import Path
from dotenv import load_dotenv
from Aplicacion.Producto.servicio_producto import ServicioProducto
from Aplicacion.Cliente.servicio_cliente import ServicioCliente
from Aplicacion.Proveedor.servicio_proveedor import ServicioProveedor
from Aplicacion.Categoria.servicio_categoria import ServicioCategoria
from Aplicacion.Localidad.servicio_localidad import ServicioLocalidad
from Infraestructura.MySQL.Producto.RepositorioProducto import RepositorioProducto
from Infraestructura.MySQL.Cliente.RepositorioCliente import RepositorioCliente
from Infraestructura.MySQL.Proveedor.RepositorioProveedor import RepositorioProveedor
from Infraestructura.MySQL.Categoria.RepositorioCategoria import RepositorioCategoria
from Infraestructura.MySQL.Localidad.RepositorioLocalidad import RepositorioLocalidad
from Infraestructura.MySQL.Provincia.RepositorioProvincia import RepositorioProvincia
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

repositorioProducto = RepositorioProducto(cnx)
servicioProducto = ServicioProducto(repositorioProducto)

repositorioCliente = RepositorioCliente(cnx)
servicioCliente = ServicioCliente(repositorioCliente, repositorioLocalidad)

repositorioProveedor = RepositorioProveedor(cnx)
servicioProveedor = ServicioProveedor(repositorioProveedor)

repositorioCategoria = RepositorioCategoria(cnx)
servicioCategoria = ServicioCategoria(repositorioCategoria)

crear_aplicacion(servicioProducto, servicioCliente, servicioProveedor, servicioCategoria)

