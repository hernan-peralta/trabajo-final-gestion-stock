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
DB_DATABASE = os.getenv("DB_DATABASE")

cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = cnx.cursor()
DB_NAME = "trabajoFinal"

lista_categorias = [{"nombre": "Construccion", "observaciones": ""},
                    {"nombre": "Herramientas electricas", "observaciones": ""},
                    {"nombre": "Herramientas manuales", "observaciones": ""},
                    {"nombre": "Industria", "observaciones": ""}, {"nombre": "Jardin", "observaciones": ""}]

lista_provincias = [{"nombre": "Buenos Aires"}, {"nombre": "Catamarca"}, {"nombre": "Chubut"}, {"nombre": "Cordoba"},
                    {"nombre": "Entre Rios"}, {"nombre": "La Pampa"}, {"nombre": "La Rioja"},
                    {"nombre": "Mendoza"}, {"nombre": "San Luis"}, {"nombre": "Santa Fe"}]

lista_localidades = [{"nombre": "Firmat", "codigo_postal": "2630", "id_provincia": 10},
                     {"nombre": "Rosario", "codigo_postal": "2000", "id_provincia": 10},
                     {"nombre": "Cordoba", "codigo_postal": "5000", "id_provincia": 4},
                     {"nombre": "La Plata", "codigo_postal": "1900", "id_provincia": 1},
                     {"nombre": "Mendoza", "codigo_postal": "5500", "id_provincia": 8}]

lista_productos = [
    {"nombre": "Taladro", "marca": "Makita", "precio_unitario": 20000, "unidades_stock": 10, "descripcion": "",
     "observaciones": ""},
    {"nombre": "Soldadora", "marca": "ESAB", "precio_unitario": 100000, "unidades_stock": 10, "descripcion": "",
     "observaciones": ""},
    {"nombre": "Llave inglesa", "marca": "Bahco", "precio_unitario": 3000, "unidades_stock": 10, "descripcion": "",
     "observaciones": ""},
    {"nombre": "Motosierra", "marca": "Husqvarna", "precio_unitario": 60000, "unidades_stock": 10, "descripcion": "",
     "observaciones": ""},
    {"nombre": "Martillo demoledor", "marca": "Bosch", "precio_unitario": 22000, "unidades_stock": 10, "descripcion": "",
     "observaciones": ""}]

lista_categorias_productos = [{"id_producto": 1, "id_categoria": 1}, {"id_producto": 1, "id_categoria": 2},
                              {"id_producto": 2, "id_categoria": 2}, {"id_producto": 2, "id_categoria": 4},
                              {"id_producto": 3, "id_categoria": 3}, {"id_producto": 3, "id_categoria": 4},
                              {"id_producto": 4, "id_categoria": 5}, {"id_producto": 5, "id_categoria": 1}]

lista_clientes = [
    {"nombre": "Juan", "apellido": "Perez", "direccion": "Santa Fe 1900", "id_localidad": 1, "telefono": "425878",
     "dni": "56145646", "observaciones": ""},
    {"nombre": "Mabel", "apellido": "Garcia", "direccion": "Cordoba", "id_localidad": 1, "telefono": "425447",
     "dni": "27891454", "observaciones": ""},
    {"nombre": "Raul", "apellido": "Diaz", "direccion": "Tucuman 2588", "id_localidad": 2, "telefono": "4258775",
     "dni": "54877456", "observaciones": ""},
    {"nombre": "Antonia", "apellido": "Gonzalez", "direccion": "Sarmiento 1333", "id_localidad": 2,
     "telefono": "15548975", "dni": "35561621", "observaciones": ""}]

lista_categoria_iva = [{"categoria_iva": "IVA Responsable inscripto"},
                       {"categoria_iva": "IVA Responsable no Inscripto"}, {"categoria_iva": "Responsable monotributo"}]

lista_proveedores = [
    {"nombre": "Mayorista Cordoba", "direccion_comercial": "Cordoba 4656", "id_localidad": 3, "telefono": "456145681",
     "email": "mayoristacordoba@gmail.com", "dni": "25789402", "cbu": "4156548984531265451984",
     "id_banco": 2, "cuit": "20-25789402-1", "id_categoria_iva": 1, "observaciones": ""},
    {"nombre": "Mayorista La Plata", "direccion_comercial": "Buenos Aires 5342", "id_localidad": 4,
     "telefono": "98126156",
     "email": "mayoristalaplata@gmail.com", "dni": "26459714", "cbu": "4894561512685165489484",
     "id_banco": 1, "cuit": "20-26459714-1", "id_categoria_iva": 1, "observaciones": ""},
    {"nombre": "Mayorista Rosario", "direccion_comercial": "Santa Fe 2341", "id_localidad": 2, "telefono": "56156151",
     "email": "mayoristarosari@gmail.com", "dni": "24588456", "cbu": "1451414144284829484444",
     "id_banco": 3, "cuit": "20-24588456-1", "id_categoria_iva": 1, "observaciones": ""}]

lista_bancos = [{"nombre": "Macro", "observaciones": ""}, {"nombre": "Santander", "observaciones": ""},
                {"nombre": "Nacion", "observaciones": ""}]

lista_forma_pago = [{"forma_pago": "efectivo"}, {"forma_pago": "tarjeta de credito"},
                    {"forma_pago": "tarjeta de debito"}, {"forma_pago": "cheque"}]

agrega_categorias = ("INSERT INTO categorias "
                     "(nombre, observaciones) "
                     "VALUES (%(nombre)s, %(observaciones)s)")

agrega_provincias = ("INSERT INTO provincias "
                     "(nombre) "
                     "VALUES (%(nombre)s)")

agrega_localidades = ("INSERT INTO localidades "
                      "(nombre, codigo_postal, id_provincia) "
                      "VALUES (%(nombre)s, %(codigo_postal)s, %(id_provincia)s)")

agrega_productos = ("INSERT INTO productos "
                    "(nombre, marca, precio_unitario, unidades_stock, descripcion, observaciones) "
                    "VALUES (%(nombre)s, %(marca)s, %(precio_unitario)s, %(unidades_stock)s, %(descripcion)s, %(observaciones)s)")

agrega_categorias_productos = ("INSERT INTO categorias_productos "
                               "(id_producto, id_categoria) "
                               "VALUES (%(id_producto)s, %(id_categoria)s)")

agrega_clientes = ("INSERT INTO clientes "
                   "(nombre, apellido, direccion, id_localidad, telefono, dni, observaciones) "
                   "VALUES (%(nombre)s, %(apellido)s, %(direccion)s, %(id_localidad)s, %(telefono)s, %(dni)s, %(observaciones)s)")

agrega_categoria_iva = ("INSERT INTO categoria_iva "
                        "(categoria_iva) "
                        "VALUES (%(categoria_iva)s)")

agrega_proveedores = ("INSERT INTO proveedores "
                      "(nombre, direccion_comercial, id_localidad, telefono, email, dni, cbu, id_banco, cuit, id_categoria_iva, observaciones) "
                      "VALUES (%(nombre)s, %(direccion_comercial)s, %(id_localidad)s, %(telefono)s, %(email)s, %(dni)s, %(cbu)s, %(id_banco)s, %(cuit)s, %(id_categoria_iva)s, %(observaciones)s)")

agrega_bancos = ("INSERT INTO bancos "
                 "(nombre, observaciones) "
                 "VALUES (%(nombre)s, %(observaciones)s)")

agrega_forma_pagos = ("INSERT INTO forma_pago "
                      "(forma_pago) "
                      "VALUES (%(forma_pago)s)")


def use_database(cursor, db_name):
    try:
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("La base de datos {} no existe.".format(db_name))
        print(err)
        exit(1)


# def seed_database(cursor):
#     try:
#         cursor.execute("USE {}".format(db_name))
#     except mysql.connector.Error as err:
#         print("La base de datos {} no existe.".format(db_name))
#         if err.errno == errorcode.ER_BAD_DB_ERROR:
#             print(err)
#             exit(1)


use_database(cursor, DB_NAME)
# seed_database(TABLES)

for provincia in lista_provincias:
    cursor.execute(agrega_provincias, provincia)

for localidad in lista_localidades:
    cursor.execute(agrega_localidades, localidad)
cnx.commit()

for categoria_iva in lista_categoria_iva:
    cursor.execute(agrega_categoria_iva, categoria_iva)
cnx.commit()

for categoria in lista_categorias:
    cursor.execute(agrega_categorias, categoria)

for producto in lista_productos:
    cursor.execute(agrega_productos, producto)
cnx.commit()

for categoria_producto in lista_categorias_productos:
    cursor.execute(agrega_categorias_productos, categoria_producto)

for cliente in lista_clientes:
    cursor.execute(agrega_clientes, cliente)

for banco in lista_bancos:
    cursor.execute(agrega_bancos, banco)
cnx.commit()

for proveedor in lista_proveedores:
    cursor.execute(agrega_proveedores, proveedor)
cnx.commit()

for forma_pago in lista_forma_pago:
    cursor.execute(agrega_forma_pagos, forma_pago)
cnx.commit()

cursor.close()
cnx.close()
