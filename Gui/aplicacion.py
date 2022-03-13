import sys
from PyQt5.QtWidgets import *
from Gui.ui import *


class Gui(QMainWindow):
    def __init__(self, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria, servicio_localidad,
                 servicio_banco, servicio_detalle_venta, servicio_venta):
        super().__init__()

        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria,
                             servicio_localidad, servicio_banco, servicio_detalle_venta, servicio_venta)
        self.show()


def crear_aplicacion(servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria, servicio_localidad,
                     servicio_banco, servicio_detalle_venta, servicio_venta):
    application = QApplication(sys.argv)
    dialog = Gui(servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria, servicio_localidad,
                 servicio_banco, servicio_detalle_venta, servicio_venta)
    dialog.show()
    sys.exit(application.exec_())
