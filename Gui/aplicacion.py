import sys
from PyQt5.QtWidgets import *
from Gui.trabajo import *


class Gui(QMainWindow):
    def __init__(self, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria):
        super().__init__()

        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria)
        self.show()


def crear_aplicacion(servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria):
    application = QApplication(sys.argv)
    dialog = Gui(servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria)
    dialog.show()
    sys.exit(application.exec_())
