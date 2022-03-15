import sys
from PyQt5.QtWidgets import *
from Gui.ui import *


class Gui(QMainWindow):
    def __init__(self, servicios):
        super().__init__()

        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self, servicios)
        self.show()


def crear_aplicacion(servicios):
    application = QApplication(sys.argv)
    dialog = Gui(servicios)
    dialog.show()
    sys.exit(application.exec_())
