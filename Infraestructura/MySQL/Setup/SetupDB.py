import os
from pathlib import Path
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = cnx.cursor()
DB_NAME = "trabajoFinal"
TABLES = {}

TABLES["productos"] = (
    "CREATE TABLE `productos` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `nombre` varchar(100) NOT NULL,"
    "   `marca` varchar(100) NOT NULL,"
    "   `precio_unitario` int(100) NOT NULL,"
    "   `unidades_stock` int(100) NOT NULL,"
    "   `descripcion` varchar(500),"
    "   `observaciones` varchar(500)"
    ") ENGINE=InnoDB")

TABLES["categorias"] = (
    "CREATE TABLE `categorias` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `nombre` varchar(100) NOT NULL,"
    "   `observaciones` varchar(500)"
    ") ENGINE=InnoDB")

TABLES["categorias_productos"] = (
    "CREATE TABLE `categorias_productos` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `id_producto` int(10),"
    "   `id_categoria` int(10),"
    "   FOREIGN KEY(id_producto) REFERENCES productos(id),"
    "   FOREIGN KEY(id_categoria) REFERENCES categorias(id)"
    ") ENGINE=InnoDB")

TABLES["provincias"] = (
    "CREATE TABLE `provincias` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `nombre` varchar(100) NOT NULL"
    ") ENGINE=InnoDB")

TABLES["localidades"] = (
    "CREATE TABLE `localidades` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `nombre` varchar(100) NOT NULL,"
    "   `codigo_postal` varchar(10) NOT NULL,"
    "   `id_provincia` int(10),"
    "   FOREIGN KEY(id_provincia) REFERENCES provincias(id)"
    ") ENGINE=InnoDB")

TABLES["clientes"] = (
    "CREATE TABLE `clientes` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `nombre` varchar(100) NOT NULL,"
    "   `apellido` varchar(100) NOT NULL,"
    "   `direccion` varchar(100) NOT NULL,"
    "   `id_localidad` int(10) NOT NULL,"
    "   `telefono` varchar(20),"
    "   `dni` varchar(10),"
    "   `observaciones` varchar(500) NOT NULL,"
    "   FOREIGN KEY(id_localidad) REFERENCES localidades(id)"
    ") ENGINE=InnoDB")

TABLES["categoria_iva"] = (
    "CREATE TABLE `categoria_iva` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `categoria_iva` varchar(100) NOT NULL"
    ") ENGINE=InnoDB")

TABLES["proveedores"] = (
    "CREATE TABLE `proveedores` ("
    "   `id` int(10) PRIMARY KEY AUTO_INCREMENT,"
    "   `nombre` varchar(100) NOT NULL,"
    "   `direccion_comercial` varchar(100) NOT NULL,"
    "   `id_localidad` int(10) NOT NULL,"
    "   `telefono` varchar(20),"
    "   `email` varchar(100) NOT NULL,"
    "   `dni` varchar(10),"
    "   `cbu` varchar(22) NOT NULL,"
    "   `banco_cbu` varchar(100) NOT NULL,"
    "   `cuit` varchar(15) NOT NULL,"
    "   `id_categoria_iva` int(10) NOT NULL,"
    "   `observaciones` varchar(500) NOT NULL,"
    "   FOREIGN KEY(id_localidad) REFERENCES localidades(id),"
    "   FOREIGN KEY(id_categoria_iva) REFERENCES categoria_iva(id)"
    ") ENGINE=InnoDB")


def create_database(cursor, db_name):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Hubo un error al crear la base de datos: {}".format(err))
        exit(1)


def use_database(cursor, db_name):
    try:
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("La base de datos {} no existe.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, db_name)
            print("La base de datos {} se creó exitosamente.".format(db_name))
            cnx.database = db_name
        else:
            print(err)
            exit(1)


def create_tables(tables):
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Creando tabla {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("ya existe.")
            else:
                print(err.msg)
        else:
            print("OK")


create_database(cursor, DB_NAME)
use_database(cursor, DB_NAME)
create_tables(TABLES)
cnx.close()
