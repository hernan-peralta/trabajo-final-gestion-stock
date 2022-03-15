# Trabajo final Programación I / Base de datos I

## Descripción
Sistema de gestión de stock de productos, proveedores, clientes, compras y ventas escrito en Python, Qt y MySQL

## Requerimientos:
* Python 3.8
* [Poetry](https://python-poetry.org/)
* Docker
* docker-compose

## Instalación y ejecución:
1) Ejecutar `poetry install` para instalar dependencias
2) Ejecutar `docker-compose up` en el directorio raíz del proyecto
3) Ejecutar `python3 Infraestructura/Mysql/Setup/SetupDB.py`
4) Ejecutar `python3 Infraestructura/Mysql/Setup/SeedDB.py` (Opcional)
5) Ejecutar `python3 bootstrap.py`

## Diagramas

![Diagrama entidades](diagrama%20entidades.png)

![Diagrama relaciones](diagrama%20relaciones.png)

![Diagrama tablas](diagrama%20tablas.png)
