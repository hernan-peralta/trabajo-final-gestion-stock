# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    cantidad_filas = 10
    cantidad_elementos_productoDto = 8
    cantidad_elementos_clienteDto = 8
    cantidad_elementos_proveedorDto = 12
    cantidad_elementos_categoriaDto = 3
    cantidad_elementos_localidadDto = 4
    cantidad_elementos_bancoDto = 3
    cantidad_elementos_detalle_ventas = 4
    cantidad_elementos_ventas = 5
    cantidad_elementos_detalle_compras = 4
    cantidad_elementos_compras = 5

    def setupUi(self, MainWindow, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria,
                servicio_localidad, servicio_banco, servicio_detalle_venta, servicio_venta):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1259, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidgetAplicacion = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetAplicacion.setGeometry(QtCore.QRect(0, 10, 1251, 801))
        self.tabWidgetAplicacion.setObjectName("tabWidgetAplicacion")
        self.tab_producto = QtWidgets.QWidget()
        self.tab_producto.setObjectName("tab_producto")
        self.tabWidgetProducto = QtWidgets.QTabWidget(self.tab_producto)
        self.tabWidgetProducto.setGeometry(QtCore.QRect(0, 0, 1231, 761))
        self.tabWidgetProducto.setObjectName("tabWidgetProducto")
        self.tab_listado_producto = QtWidgets.QWidget()
        self.tab_listado_producto.setObjectName("tab_listado_producto")
        self.frame_buscar_producto = QtWidgets.QFrame(self.tab_listado_producto)
        self.frame_buscar_producto.setGeometry(QtCore.QRect(60, 10, 861, 101))
        self.frame_buscar_producto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_producto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_producto.setObjectName("frame_buscar_producto")
        self.comboBox_atributo_busqueda_producto = QtWidgets.QComboBox(self.frame_buscar_producto)
        self.comboBox_atributo_busqueda_producto.setGeometry(QtCore.QRect(70, 30, 106, 28))
        self.comboBox_atributo_busqueda_producto.setObjectName("comboBox_atributo_busqueda_producto")
        self.comboBox_atributo_busqueda_producto.addItem("")
        self.comboBox_atributo_busqueda_producto.addItem("")
        self.comboBox_atributo_busqueda_producto.addItem("")
        self.comboBox_atributo_busqueda_producto.addItem("")
        self.btn_buscar_producto = QtWidgets.QPushButton(self.frame_buscar_producto)
        self.btn_buscar_producto.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_producto.setObjectName("btn_buscar_producto")
        self.lineEdit_buscar_producto = QtWidgets.QLineEdit(self.frame_buscar_producto)
        self.lineEdit_buscar_producto.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_producto.setObjectName("lineEdit_buscar_producto")
        self.tableResultadoBusquedaProducto = QtWidgets.QTableWidget(self.tab_listado_producto)
        self.tableResultadoBusquedaProducto.setEnabled(True)
        self.tableResultadoBusquedaProducto.setGeometry(QtCore.QRect(20, 190, 1171, 511))
        self.tableResultadoBusquedaProducto.setAcceptDrops(False)
        self.tableResultadoBusquedaProducto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableResultadoBusquedaProducto.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableResultadoBusquedaProducto.setLineWidth(1)
        self.tableResultadoBusquedaProducto.setMidLineWidth(0)
        self.tableResultadoBusquedaProducto.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableResultadoBusquedaProducto.setShowGrid(True)
        self.tableResultadoBusquedaProducto.setWordWrap(True)
        self.tableResultadoBusquedaProducto.setCornerButtonEnabled(True)
        self.tableResultadoBusquedaProducto.setRowCount(20)
        self.tableResultadoBusquedaProducto.setObjectName("tableResultadoBusquedaProducto")
        self.tableResultadoBusquedaProducto.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResultadoBusquedaProducto.setHorizontalHeaderItem(7, item)
        self.tableResultadoBusquedaProducto.horizontalHeader().setCascadingSectionResizes(False)
        self.btn_mostrar_todos_productos = QtWidgets.QPushButton(self.tab_listado_producto)
        self.btn_mostrar_todos_productos.setGeometry(QtCore.QRect(250, 140, 552, 28))
        self.btn_mostrar_todos_productos.setObjectName("btn_mostrar_todos_productos")
        self.tabWidgetProducto.addTab(self.tab_listado_producto, "")
        self.tab_agregar_modificar_producto = QtWidgets.QWidget()
        self.tab_agregar_modificar_producto.setObjectName("tab_agregar_modificar_producto")
        self.frame = QtWidgets.QFrame(self.tab_agregar_modificar_producto)
        self.frame.setGeometry(QtCore.QRect(90, 110, 831, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_agregar_producto_nombre = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_nombre.setObjectName("label_agregar_producto_nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_nombre)
        self.lineEdit_agregar_producto_nombre = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_nombre.setObjectName("lineEdit_agregar_producto_nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_nombre)
        self.label_agregar_producto_marca = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_marca.setObjectName("label_agregar_producto_marca")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_marca)
        self.lineEdit_agregar_producto_marca = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_marca.setObjectName("lineEdit_agregar_producto_marca")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_marca)
        self.label_agregar_producto_categoria = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_categoria.setObjectName("label_agregar_producto_categoria")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_categoria)
        self.label_agregar_producto_precio_unitario = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_precio_unitario.setObjectName("label_agregar_producto_precio_unitario")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_precio_unitario)
        self.lineEdit_agregar_producto_precio_unitario = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_precio_unitario.setObjectName("lineEdit_agregar_producto_precio_unitario")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_precio_unitario)
        self.label_agregar_producto_precio_unitario_2 = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_precio_unitario_2.setObjectName("label_agregar_producto_precio_unitario_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_precio_unitario_2)
        self.lineEdit_agregar_producto_unidades_stock = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_unidades_stock.setObjectName("lineEdit_agregar_producto_unidades_stock")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_unidades_stock)
        self.label_agregar_producto_proveedor = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_proveedor.setObjectName("label_agregar_producto_proveedor")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_proveedor)
        self.label_agregar_producto_descripcion = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_descripcion.setObjectName("label_agregar_producto_descripcion")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_descripcion)
        self.lineEdit_agregar_producto_descripcion = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_descripcion.setObjectName("lineEdit_agregar_producto_descripcion")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_descripcion)
        self.label_agregar_producto_observaciones = QtWidgets.QLabel(self.frame)
        self.label_agregar_producto_observaciones.setObjectName("label_agregar_producto_observaciones")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_agregar_producto_observaciones)
        self.lineEdit_agregar_producto_observaciones = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_observaciones.setObjectName("lineEdit_agregar_producto_observaciones")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_observaciones)
        self.pushButton_agregar_producto_guardar = QtWidgets.QPushButton(self.frame)
        self.pushButton_agregar_producto_guardar.setObjectName("pushButton_agregar_producto_guardar")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.pushButton_agregar_producto_guardar)
        self.pushButton_actualizar_producto = QtWidgets.QPushButton(self.frame)
        self.pushButton_actualizar_producto.setObjectName("pushButton_actualizar_producto")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.pushButton_actualizar_producto)
        self.lineEdit_agregar_producto_categoria = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_categoria.setObjectName("lineEdit_agregar_producto_categoria")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_categoria)
        self.lineEdit_agregar_producto_proveedores = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_agregar_producto_proveedores.setObjectName("lineEdit_agregar_producto_proveedores")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_agregar_producto_proveedores)
        self.frame_3 = QtWidgets.QFrame(self.tab_agregar_modificar_producto)
        self.frame_3.setGeometry(QtCore.QRect(90, 20, 831, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_buscar_producto_por_id = QtWidgets.QLabel(self.frame_3)
        self.label_buscar_producto_por_id.setGeometry(QtCore.QRect(20, 20, 64, 28))
        self.label_buscar_producto_por_id.setObjectName("label_buscar_producto_por_id")
        self.lineEdit_buscar_producto_por_id = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_buscar_producto_por_id.setGeometry(QtCore.QRect(110, 20, 511, 28))
        self.lineEdit_buscar_producto_por_id.setObjectName("lineEdit_buscar_producto_por_id")
        self.pushButton_cargar_producto_desde_id = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_cargar_producto_desde_id.setGeometry(QtCore.QRect(630, 20, 191, 28))
        self.pushButton_cargar_producto_desde_id.setObjectName("pushButton_cargar_producto_desde_id")
        self.frame_3.raise_()
        self.frame.raise_()
        self.tabWidgetProducto.addTab(self.tab_agregar_modificar_producto, "")
        self.tab_eliminar_producto = QtWidgets.QWidget()
        self.tab_eliminar_producto.setObjectName("tab_eliminar_producto")
        self.frame_8 = QtWidgets.QFrame(self.tab_eliminar_producto)
        self.frame_8.setGeometry(QtCore.QRect(80, 40, 841, 521))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.formLayout_7 = QtWidgets.QFormLayout(self.frame_8)
        self.formLayout_7.setObjectName("formLayout_7")
        self.pushButton_eliminarProducto = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_eliminarProducto.setObjectName("pushButton_eliminarProducto")
        self.formLayout_7.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_eliminarProducto)
        self.lineEdit_eliminar_idProducto = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_eliminar_idProducto.setObjectName("lineEdit_eliminar_idProducto")
        self.formLayout_7.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eliminar_idProducto)
        self.label_eliminar_idProducto = QtWidgets.QLabel(self.frame_8)
        self.label_eliminar_idProducto.setObjectName("label_eliminar_idProducto")
        self.formLayout_7.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_eliminar_idProducto)
        self.tabWidgetProducto.addTab(self.tab_eliminar_producto, "")
        self.tabWidgetAplicacion.addTab(self.tab_producto, "")
        self.tab_cliente = QtWidgets.QWidget()
        self.tab_cliente.setObjectName("tab_cliente")
        self.tabWidgetCliente = QtWidgets.QTabWidget(self.tab_cliente)
        self.tabWidgetCliente.setGeometry(QtCore.QRect(0, 0, 1221, 761))
        self.tabWidgetCliente.setObjectName("tabWidgetCliente")
        self.tab_listado_cliente = QtWidgets.QWidget()
        self.tab_listado_cliente.setObjectName("tab_listado_cliente")
        self.tableListaCliente = QtWidgets.QTableWidget(self.tab_listado_cliente)
        self.tableListaCliente.setEnabled(True)
        self.tableListaCliente.setGeometry(QtCore.QRect(10, 190, 1181, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableListaCliente.sizePolicy().hasHeightForWidth())
        self.tableListaCliente.setSizePolicy(sizePolicy)
        self.tableListaCliente.setAcceptDrops(False)
        self.tableListaCliente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaCliente.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaCliente.setLineWidth(1)
        self.tableListaCliente.setMidLineWidth(0)
        self.tableListaCliente.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaCliente.setShowGrid(True)
        self.tableListaCliente.setWordWrap(True)
        self.tableListaCliente.setCornerButtonEnabled(True)
        self.tableListaCliente.setRowCount(20)
        self.tableListaCliente.setColumnCount(8)
        self.tableListaCliente.setObjectName("tableListaCliente")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCliente.setHorizontalHeaderItem(7, item)
        self.tableListaCliente.horizontalHeader().setCascadingSectionResizes(False)
        self.frame_buscar_cliente = QtWidgets.QFrame(self.tab_listado_cliente)
        self.frame_buscar_cliente.setGeometry(QtCore.QRect(60, 10, 811, 111))
        self.frame_buscar_cliente.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_cliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_cliente.setObjectName("frame_buscar_cliente")
        self.comboBox_atributo_busqueda_cliente = QtWidgets.QComboBox(self.frame_buscar_cliente)
        self.comboBox_atributo_busqueda_cliente.setGeometry(QtCore.QRect(70, 30, 106, 28))
        self.comboBox_atributo_busqueda_cliente.setObjectName("comboBox_atributo_busqueda_cliente")
        self.comboBox_atributo_busqueda_cliente.addItem("")
        self.comboBox_atributo_busqueda_cliente.addItem("")
        self.comboBox_atributo_busqueda_cliente.addItem("")
        self.comboBox_atributo_busqueda_cliente.addItem("")
        self.btn_buscar_cliente = QtWidgets.QPushButton(self.frame_buscar_cliente)
        self.btn_buscar_cliente.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_cliente.setObjectName("btn_buscar_cliente")
        self.lineEdit_buscar_cliente = QtWidgets.QLineEdit(self.frame_buscar_cliente)
        self.lineEdit_buscar_cliente.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_cliente.setObjectName("lineEdit_buscar_cliente")
        self.btn_mostrar_todos_clientes = QtWidgets.QPushButton(self.tab_listado_cliente)
        self.btn_mostrar_todos_clientes.setGeometry(QtCore.QRect(250, 140, 552, 28))
        self.btn_mostrar_todos_clientes.setObjectName("btn_mostrar_todos_clientes")
        self.tabWidgetCliente.addTab(self.tab_listado_cliente, "")
        self.tab_agregar_modificar_cliente = QtWidgets.QWidget()
        self.tab_agregar_modificar_cliente.setObjectName("tab_agregar_modificar_cliente")
        self.frame_2 = QtWidgets.QFrame(self.tab_agregar_modificar_cliente)
        self.frame_2.setGeometry(QtCore.QRect(110, 150, 831, 441))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_nombreCliente = QtWidgets.QLabel(self.frame_2)
        self.label_nombreCliente.setObjectName("label_nombreCliente")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_nombreCliente)
        self.lineEdit_nombreCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_nombreCliente.setObjectName("lineEdit_nombreCliente")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombreCliente)
        self.label_apellidoCliente = QtWidgets.QLabel(self.frame_2)
        self.label_apellidoCliente.setObjectName("label_apellidoCliente")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_apellidoCliente)
        self.lineEdit_apellidoCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_apellidoCliente.setObjectName("lineEdit_apellidoCliente")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_apellidoCliente)
        self.label_direccionCliente = QtWidgets.QLabel(self.frame_2)
        self.label_direccionCliente.setObjectName("label_direccionCliente")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_direccionCliente)
        self.lineEdit_direccionCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_direccionCliente.setObjectName("lineEdit_direccionCliente")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_direccionCliente)
        self.label_localidadCliente = QtWidgets.QLabel(self.frame_2)
        self.label_localidadCliente.setObjectName("label_localidadCliente")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_localidadCliente)
        self.lineEdit_localidadCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_localidadCliente.setObjectName("lineEdit_localidadCliente")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.lineEdit_localidadCliente)
        self.label_telefonoCliente = QtWidgets.QLabel(self.frame_2)
        self.label_telefonoCliente.setObjectName("label_telefonoCliente")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_telefonoCliente)
        self.lineEdit_telefonoCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_telefonoCliente.setObjectName("lineEdit_telefonoCliente")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.lineEdit_telefonoCliente)
        self.label_dniCliente = QtWidgets.QLabel(self.frame_2)
        self.label_dniCliente.setObjectName("label_dniCliente")
        self.formLayout_2.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_dniCliente)
        self.lineEdit_dniCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_dniCliente.setObjectName("lineEdit_dniCliente")
        self.formLayout_2.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dniCliente)
        self.label_observacionesCliente = QtWidgets.QLabel(self.frame_2)
        self.label_observacionesCliente.setObjectName("label_observacionesCliente")
        self.formLayout_2.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_observacionesCliente)
        self.lineEdit_observacionesCliente = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_observacionesCliente.setObjectName("lineEdit_observacionesCliente")
        self.formLayout_2.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.lineEdit_observacionesCliente)
        self.pushButton_guardarCliente = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_guardarCliente.setObjectName("pushButton_guardarCliente")
        self.formLayout_2.setWidget(24, QtWidgets.QFormLayout.FieldRole, self.pushButton_guardarCliente)
        self.pushButton_actualizarCliente = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_actualizarCliente.setObjectName("pushButton_actualizarCliente")
        self.formLayout_2.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_actualizarCliente)
        self.frame_10 = QtWidgets.QFrame(self.tab_agregar_modificar_cliente)
        self.frame_10.setGeometry(QtCore.QRect(110, 40, 831, 80))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_buscar_cliente_por_id = QtWidgets.QLabel(self.frame_10)
        self.label_buscar_cliente_por_id.setGeometry(QtCore.QRect(20, 20, 64, 28))
        self.label_buscar_cliente_por_id.setObjectName("label_buscar_cliente_por_id")
        self.lineEdit_buscar_cliente_por_id = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_buscar_cliente_por_id.setGeometry(QtCore.QRect(110, 20, 511, 28))
        self.lineEdit_buscar_cliente_por_id.setObjectName("lineEdit_buscar_cliente_por_id")
        self.pushButton_cargar_cliente_desde_id = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_cargar_cliente_desde_id.setGeometry(QtCore.QRect(630, 20, 191, 28))
        self.pushButton_cargar_cliente_desde_id.setObjectName("pushButton_cargar_cliente_desde_id")
        self.tabWidgetCliente.addTab(self.tab_agregar_modificar_cliente, "")
        self.tab_eliminar_cliente = QtWidgets.QWidget()
        self.tab_eliminar_cliente.setObjectName("tab_eliminar_cliente")
        self.frame_7 = QtWidgets.QFrame(self.tab_eliminar_cliente)
        self.frame_7.setGeometry(QtCore.QRect(70, 30, 841, 521))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_6.setObjectName("formLayout_6")
        self.pushButton_eliminarCliente = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_eliminarCliente.setObjectName("pushButton_eliminarCliente")
        self.formLayout_6.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_eliminarCliente)
        self.lineEdit_eliminar_idCliente = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_eliminar_idCliente.setObjectName("lineEdit_eliminar_idCliente")
        self.formLayout_6.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eliminar_idCliente)
        self.label_eliminar_idCliente = QtWidgets.QLabel(self.frame_7)
        self.label_eliminar_idCliente.setObjectName("label_eliminar_idCliente")
        self.formLayout_6.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_eliminar_idCliente)
        self.tabWidgetCliente.addTab(self.tab_eliminar_cliente, "")
        self.tabWidgetAplicacion.addTab(self.tab_cliente, "")
        self.tab_proveedor = QtWidgets.QWidget()
        self.tab_proveedor.setObjectName("tab_proveedor")
        self.tabWidgetProveedor = QtWidgets.QTabWidget(self.tab_proveedor)
        self.tabWidgetProveedor.setGeometry(QtCore.QRect(0, 0, 1231, 761))
        self.tabWidgetProveedor.setObjectName("tabWidgetProveedor")
        self.tab_listado_proveedor = QtWidgets.QWidget()
        self.tab_listado_proveedor.setObjectName("tab_listado_proveedor")
        self.tableListaProveedor = QtWidgets.QTableWidget(self.tab_listado_proveedor)
        self.tableListaProveedor.setEnabled(True)
        self.tableListaProveedor.setGeometry(QtCore.QRect(20, 190, 1191, 521))
        self.tableListaProveedor.setAcceptDrops(False)
        self.tableListaProveedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaProveedor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaProveedor.setLineWidth(1)
        self.tableListaProveedor.setMidLineWidth(0)
        self.tableListaProveedor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaProveedor.setShowGrid(True)
        self.tableListaProveedor.setWordWrap(True)
        self.tableListaProveedor.setCornerButtonEnabled(True)
        self.tableListaProveedor.setRowCount(20)
        self.tableListaProveedor.setColumnCount(12)
        self.tableListaProveedor.setObjectName("tableListaProveedor")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaProveedor.setHorizontalHeaderItem(11, item)
        self.tableListaProveedor.horizontalHeader().setCascadingSectionResizes(False)
        self.frame_buscar_proveedor = QtWidgets.QFrame(self.tab_listado_proveedor)
        self.frame_buscar_proveedor.setGeometry(QtCore.QRect(140, 10, 811, 111))
        self.frame_buscar_proveedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_proveedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_proveedor.setObjectName("frame_buscar_proveedor")
        self.comboBox_atributo_busqueda_proveedor = QtWidgets.QComboBox(self.frame_buscar_proveedor)
        self.comboBox_atributo_busqueda_proveedor.setGeometry(QtCore.QRect(70, 30, 106, 28))
        self.comboBox_atributo_busqueda_proveedor.setObjectName("comboBox_atributo_busqueda_proveedor")
        self.comboBox_atributo_busqueda_proveedor.addItem("")
        self.comboBox_atributo_busqueda_proveedor.addItem("")
        self.comboBox_atributo_busqueda_proveedor.addItem("")
        self.btn_buscar_proveedor = QtWidgets.QPushButton(self.frame_buscar_proveedor)
        self.btn_buscar_proveedor.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_proveedor.setObjectName("btn_buscar_proveedor")
        self.lineEdit_buscar_proveedor = QtWidgets.QLineEdit(self.frame_buscar_proveedor)
        self.lineEdit_buscar_proveedor.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_proveedor.setObjectName("lineEdit_buscar_proveedor")
        self.btn_mostrar_todos_proveedores = QtWidgets.QPushButton(self.tab_listado_proveedor)
        self.btn_mostrar_todos_proveedores.setGeometry(QtCore.QRect(330, 140, 552, 28))
        self.btn_mostrar_todos_proveedores.setObjectName("btn_mostrar_todos_proveedores")
        self.tabWidgetProveedor.addTab(self.tab_listado_proveedor, "")
        self.tab_agregar_modificar_proveedor = QtWidgets.QWidget()
        self.tab_agregar_modificar_proveedor.setObjectName("tab_agregar_modificar_proveedor")
        self.frame_5 = QtWidgets.QFrame(self.tab_agregar_modificar_proveedor)
        self.frame_5.setGeometry(QtCore.QRect(120, 100, 841, 561))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_nombreProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_nombreProveedor.setObjectName("label_nombreProveedor")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_nombreProveedor)
        self.lineEdit_nombreProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_nombreProveedor.setObjectName("lineEdit_nombreProveedor")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombreProveedor)
        self.label_direccionComercialProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_direccionComercialProveedor.setObjectName("label_direccionComercialProveedor")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_direccionComercialProveedor)
        self.lineEdit_direccionComercialProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_direccionComercialProveedor.setObjectName("lineEdit_direccionComercialProveedor")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_direccionComercialProveedor)
        self.label_localidadProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_localidadProveedor.setObjectName("label_localidadProveedor")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_localidadProveedor)
        self.lineEdit_localidadProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_localidadProveedor.setObjectName("lineEdit_localidadProveedor")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_localidadProveedor)
        self.label_telefonoProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_telefonoProveedor.setObjectName("label_telefonoProveedor")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_telefonoProveedor)
        self.lineEdit_telefonoProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_telefonoProveedor.setObjectName("lineEdit_telefonoProveedor")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_telefonoProveedor)
        self.label_emailProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_emailProveedor.setObjectName("label_emailProveedor")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_emailProveedor)
        self.lineEdit_emailProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_emailProveedor.setObjectName("lineEdit_emailProveedor")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_emailProveedor)
        self.label_dniProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_dniProveedor.setObjectName("label_dniProveedor")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_dniProveedor)
        self.lineEdit_dniProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_dniProveedor.setObjectName("lineEdit_dniProveedor")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dniProveedor)
        self.label_cbuProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_cbuProveedor.setObjectName("label_cbuProveedor")
        self.formLayout_4.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_cbuProveedor)
        self.lineEdit_cbuProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_cbuProveedor.setObjectName("lineEdit_cbuProveedor")
        self.formLayout_4.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_cbuProveedor)
        self.label_bancoCbuProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_bancoCbuProveedor.setObjectName("label_bancoCbuProveedor")
        self.formLayout_4.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_bancoCbuProveedor)
        self.lineEdit_bancoCbuProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_bancoCbuProveedor.setObjectName("lineEdit_bancoCbuProveedor")
        self.formLayout_4.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.lineEdit_bancoCbuProveedor)
        self.label_cuitProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_cuitProveedor.setObjectName("label_cuitProveedor")
        self.formLayout_4.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_cuitProveedor)
        self.lineEdit_cuitProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_cuitProveedor.setObjectName("lineEdit_cuitProveedor")
        self.formLayout_4.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.lineEdit_cuitProveedor)
        self.label_categoriaIvaProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_categoriaIvaProveedor.setObjectName("label_categoriaIvaProveedor")
        self.formLayout_4.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_categoriaIvaProveedor)
        self.lineEdit_categoriaIvaProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_categoriaIvaProveedor.setObjectName("lineEdit_categoriaIvaProveedor")
        self.formLayout_4.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.lineEdit_categoriaIvaProveedor)
        self.label_observacionesProveedor = QtWidgets.QLabel(self.frame_5)
        self.label_observacionesProveedor.setObjectName("label_observacionesProveedor")
        self.formLayout_4.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_observacionesProveedor)
        self.lineEdit_observacionesProveedor = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_observacionesProveedor.setObjectName("lineEdit_observacionesProveedor")
        self.formLayout_4.setWidget(24, QtWidgets.QFormLayout.FieldRole, self.lineEdit_observacionesProveedor)
        self.pushButton_guardarProveedor = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_guardarProveedor.setObjectName("pushButton_guardarProveedor")
        self.formLayout_4.setWidget(29, QtWidgets.QFormLayout.FieldRole, self.pushButton_guardarProveedor)
        self.pushButton_actualizarProveedor = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_actualizarProveedor.setObjectName("pushButton_actualizarProveedor")
        self.formLayout_4.setWidget(30, QtWidgets.QFormLayout.FieldRole, self.pushButton_actualizarProveedor)
        self.frame_11 = QtWidgets.QFrame(self.tab_agregar_modificar_proveedor)
        self.frame_11.setGeometry(QtCore.QRect(120, 10, 841, 80))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_buscar_proveedor_por_id = QtWidgets.QLabel(self.frame_11)
        self.label_buscar_proveedor_por_id.setGeometry(QtCore.QRect(20, 20, 64, 28))
        self.label_buscar_proveedor_por_id.setObjectName("label_buscar_proveedor_por_id")
        self.lineEdit_buscar_proveedor_por_id = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_buscar_proveedor_por_id.setGeometry(QtCore.QRect(110, 20, 511, 28))
        self.lineEdit_buscar_proveedor_por_id.setObjectName("lineEdit_buscar_proveedor_por_id")
        self.pushButton_cargar_proveedor_desde_id = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_cargar_proveedor_desde_id.setGeometry(QtCore.QRect(630, 20, 191, 28))
        self.pushButton_cargar_proveedor_desde_id.setObjectName("pushButton_cargar_proveedor_desde_id")
        self.tabWidgetProveedor.addTab(self.tab_agregar_modificar_proveedor, "")
        self.tab_eliminar_proveedor = QtWidgets.QWidget()
        self.tab_eliminar_proveedor.setObjectName("tab_eliminar_proveedor")
        self.frame_6 = QtWidgets.QFrame(self.tab_eliminar_proveedor)
        self.frame_6.setGeometry(QtCore.QRect(70, 30, 841, 521))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout_5.setObjectName("formLayout_5")
        self.pushButton_eliminarProveedor = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_eliminarProveedor.setObjectName("pushButton_eliminarProveedor")
        self.formLayout_5.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_eliminarProveedor)
        self.lineEdit_eliminar_idProveedor = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_eliminar_idProveedor.setObjectName("lineEdit_eliminar_idProveedor")
        self.formLayout_5.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eliminar_idProveedor)
        self.label_eliminar_idProveedor = QtWidgets.QLabel(self.frame_6)
        self.label_eliminar_idProveedor.setObjectName("label_eliminar_idProveedor")
        self.formLayout_5.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_eliminar_idProveedor)
        self.tabWidgetProveedor.addTab(self.tab_eliminar_proveedor, "")
        self.tabWidgetAplicacion.addTab(self.tab_proveedor, "")
        self.tab_categoria = QtWidgets.QWidget()
        self.tab_categoria.setObjectName("tab_categoria")
        self.tabWidgetCliente_2 = QtWidgets.QTabWidget(self.tab_categoria)
        self.tabWidgetCliente_2.setGeometry(QtCore.QRect(0, 0, 1231, 751))
        self.tabWidgetCliente_2.setObjectName("tabWidgetCliente_2")
        self.tab_listado_categoria = QtWidgets.QWidget()
        self.tab_listado_categoria.setObjectName("tab_listado_categoria")
        self.tableListaCategoria = QtWidgets.QTableWidget(self.tab_listado_categoria)
        self.tableListaCategoria.setEnabled(True)
        self.tableListaCategoria.setGeometry(QtCore.QRect(140, 200, 1031, 491))
        self.tableListaCategoria.setAcceptDrops(False)
        self.tableListaCategoria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaCategoria.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaCategoria.setLineWidth(1)
        self.tableListaCategoria.setMidLineWidth(0)
        self.tableListaCategoria.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaCategoria.setShowGrid(True)
        self.tableListaCategoria.setWordWrap(True)
        self.tableListaCategoria.setCornerButtonEnabled(True)
        self.tableListaCategoria.setRowCount(20)
        self.tableListaCategoria.setColumnCount(3)
        self.tableListaCategoria.setObjectName("tableListaCategoria")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCategoria.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCategoria.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCategoria.setHorizontalHeaderItem(2, item)
        self.tableListaCategoria.horizontalHeader().setCascadingSectionResizes(False)
        self.frame_buscar_categoria = QtWidgets.QFrame(self.tab_listado_categoria)
        self.frame_buscar_categoria.setGeometry(QtCore.QRect(110, 10, 811, 111))
        self.frame_buscar_categoria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_categoria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_categoria.setObjectName("frame_buscar_categoria")
        self.btn_buscar_categoria = QtWidgets.QPushButton(self.frame_buscar_categoria)
        self.btn_buscar_categoria.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_categoria.setObjectName("btn_buscar_categoria")
        self.lineEdit_buscar_categoria = QtWidgets.QLineEdit(self.frame_buscar_categoria)
        self.lineEdit_buscar_categoria.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_categoria.setObjectName("lineEdit_buscar_categoria")
        self.btn_mostrar_todos_categorias = QtWidgets.QPushButton(self.tab_listado_categoria)
        self.btn_mostrar_todos_categorias.setGeometry(QtCore.QRect(300, 140, 552, 28))
        self.btn_mostrar_todos_categorias.setObjectName("btn_mostrar_todos_categorias")
        self.tabWidgetCliente_2.addTab(self.tab_listado_categoria, "")
        self.tab_agregar_modificar_categoria = QtWidgets.QWidget()
        self.tab_agregar_modificar_categoria.setObjectName("tab_agregar_modificar_categoria")
        self.frame_4 = QtWidgets.QFrame(self.tab_agregar_modificar_categoria)
        self.frame_4.setGeometry(QtCore.QRect(140, 190, 841, 291))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_nombreCategoria = QtWidgets.QLabel(self.frame_4)
        self.label_nombreCategoria.setObjectName("label_nombreCategoria")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_nombreCategoria)
        self.lineEdit_nombreCategoria = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_nombreCategoria.setObjectName("lineEdit_nombreCategoria")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombreCategoria)
        self.label_observacionesCategoria = QtWidgets.QLabel(self.frame_4)
        self.label_observacionesCategoria.setObjectName("label_observacionesCategoria")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_observacionesCategoria)
        self.lineEdit_observacionesCategoria = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_observacionesCategoria.setObjectName("lineEdit_observacionesCategoria")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_observacionesCategoria)
        self.pushButton_guardarCategoria = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_guardarCategoria.setObjectName("pushButton_guardarCategoria")
        self.formLayout_3.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.pushButton_guardarCategoria)
        self.pushButton_actualizarCategoria = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_actualizarCategoria.setObjectName("pushButton_actualizarCategoria")
        self.formLayout_3.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.pushButton_actualizarCategoria)
        self.frame_12 = QtWidgets.QFrame(self.tab_agregar_modificar_categoria)
        self.frame_12.setGeometry(QtCore.QRect(140, 60, 841, 80))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_buscar_categoria_por_id = QtWidgets.QLabel(self.frame_12)
        self.label_buscar_categoria_por_id.setGeometry(QtCore.QRect(20, 20, 64, 28))
        self.label_buscar_categoria_por_id.setObjectName("label_buscar_categoria_por_id")
        self.lineEdit_buscar_categoria_por_id = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_buscar_categoria_por_id.setGeometry(QtCore.QRect(70, 20, 511, 28))
        self.lineEdit_buscar_categoria_por_id.setObjectName("lineEdit_buscar_categoria_por_id")
        self.pushButton_cargar_categoria_desde_id = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_cargar_categoria_desde_id.setGeometry(QtCore.QRect(630, 20, 191, 28))
        self.pushButton_cargar_categoria_desde_id.setObjectName("pushButton_cargar_categoria_desde_id")
        self.tabWidgetCliente_2.addTab(self.tab_agregar_modificar_categoria, "")
        self.tab_eliminar_categoria = QtWidgets.QWidget()
        self.tab_eliminar_categoria.setObjectName("tab_eliminar_categoria")
        self.frame_9 = QtWidgets.QFrame(self.tab_eliminar_categoria)
        self.frame_9.setGeometry(QtCore.QRect(60, 30, 841, 521))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.formLayout_8 = QtWidgets.QFormLayout(self.frame_9)
        self.formLayout_8.setObjectName("formLayout_8")
        self.pushButton_eliminarCategoria = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_eliminarCategoria.setObjectName("pushButton_eliminarCategoria")
        self.formLayout_8.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_eliminarCategoria)
        self.lineEdit_eliminar_idCategoria = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_eliminar_idCategoria.setObjectName("lineEdit_eliminar_idCategoria")
        self.formLayout_8.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eliminar_idCategoria)
        self.label_eliminar_idCategoria = QtWidgets.QLabel(self.frame_9)
        self.label_eliminar_idCategoria.setObjectName("label_eliminar_idCategoria")
        self.formLayout_8.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_eliminar_idCategoria)
        self.tabWidgetCliente_2.addTab(self.tab_eliminar_categoria, "")
        self.tabWidgetAplicacion.addTab(self.tab_categoria, "")
        self.tab_localidades = QtWidgets.QWidget()
        self.tab_localidades.setObjectName("tab_localidades")
        self.tabWidgetLocalidad = QtWidgets.QTabWidget(self.tab_localidades)
        self.tabWidgetLocalidad.setGeometry(QtCore.QRect(0, 0, 1221, 761))
        self.tabWidgetLocalidad.setObjectName("tabWidgetLocalidad")
        self.tab_listado_localidad = QtWidgets.QWidget()
        self.tab_listado_localidad.setObjectName("tab_listado_localidad")
        self.tableListaLocalidad = QtWidgets.QTableWidget(self.tab_listado_localidad)
        self.tableListaLocalidad.setEnabled(True)
        self.tableListaLocalidad.setGeometry(QtCore.QRect(140, 200, 991, 491))
        self.tableListaLocalidad.setAcceptDrops(False)
        self.tableListaLocalidad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaLocalidad.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaLocalidad.setLineWidth(1)
        self.tableListaLocalidad.setMidLineWidth(0)
        self.tableListaLocalidad.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaLocalidad.setShowGrid(True)
        self.tableListaLocalidad.setWordWrap(True)
        self.tableListaLocalidad.setCornerButtonEnabled(True)
        self.tableListaLocalidad.setRowCount(20)
        self.tableListaLocalidad.setColumnCount(4)
        self.tableListaLocalidad.setObjectName("tableListaLocalidad")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaLocalidad.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaLocalidad.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaLocalidad.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaLocalidad.setHorizontalHeaderItem(3, item)
        self.tableListaLocalidad.horizontalHeader().setCascadingSectionResizes(False)
        self.frame_buscar_localidad = QtWidgets.QFrame(self.tab_listado_localidad)
        self.frame_buscar_localidad.setGeometry(QtCore.QRect(110, 10, 811, 111))
        self.frame_buscar_localidad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_localidad.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_localidad.setObjectName("frame_buscar_localidad")
        self.btn_buscar_localidad = QtWidgets.QPushButton(self.frame_buscar_localidad)
        self.btn_buscar_localidad.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_localidad.setObjectName("btn_buscar_localidad")
        self.lineEdit_buscar_localidad = QtWidgets.QLineEdit(self.frame_buscar_localidad)
        self.lineEdit_buscar_localidad.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_localidad.setObjectName("lineEdit_buscar_localidad")
        self.comboBox_atributo_busqueda_cliente_2 = QtWidgets.QComboBox(self.frame_buscar_localidad)
        self.comboBox_atributo_busqueda_cliente_2.setGeometry(QtCore.QRect(60, 30, 106, 28))
        self.comboBox_atributo_busqueda_cliente_2.setObjectName("comboBox_atributo_busqueda_cliente_2")
        self.comboBox_atributo_busqueda_cliente_2.addItem("")
        self.comboBox_atributo_busqueda_cliente_2.addItem("")
        self.comboBox_atributo_busqueda_cliente_2.addItem("")
        self.btn_mostrar_todos_localidad = QtWidgets.QPushButton(self.tab_listado_localidad)
        self.btn_mostrar_todos_localidad.setGeometry(QtCore.QRect(300, 140, 552, 28))
        self.btn_mostrar_todos_localidad.setObjectName("btn_mostrar_todos_localidad")
        self.tabWidgetLocalidad.addTab(self.tab_listado_localidad, "")
        self.tab_agregar_modificar_localidad = QtWidgets.QWidget()
        self.tab_agregar_modificar_localidad.setObjectName("tab_agregar_modificar_localidad")
        self.frame_13 = QtWidgets.QFrame(self.tab_agregar_modificar_localidad)
        self.frame_13.setGeometry(QtCore.QRect(140, 180, 841, 291))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.formLayout_9 = QtWidgets.QFormLayout(self.frame_13)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_nombreLocalidad = QtWidgets.QLabel(self.frame_13)
        self.label_nombreLocalidad.setObjectName("label_nombreLocalidad")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_nombreLocalidad)
        self.lineEdit_nombreLocalidad = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_nombreLocalidad.setObjectName("lineEdit_nombreLocalidad")
        self.formLayout_9.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombreLocalidad)
        self.label_codigo_postal_Localidad = QtWidgets.QLabel(self.frame_13)
        self.label_codigo_postal_Localidad.setObjectName("label_codigo_postal_Localidad")
        self.formLayout_9.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_codigo_postal_Localidad)
        self.lineEdit_codigo_postal_Localidad = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_codigo_postal_Localidad.setObjectName("lineEdit_codigo_postal_Localidad")
        self.formLayout_9.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_codigo_postal_Localidad)
        self.label_provinciaLocalidad = QtWidgets.QLabel(self.frame_13)
        self.label_provinciaLocalidad.setObjectName("label_provinciaLocalidad")
        self.formLayout_9.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_provinciaLocalidad)
        self.lineEdit_provinciaLocalidad = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_provinciaLocalidad.setObjectName("lineEdit_provinciaLocalidad")
        self.formLayout_9.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_provinciaLocalidad)
        self.pushButton_guardarLocalidad = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_guardarLocalidad.setObjectName("pushButton_guardarLocalidad")
        self.formLayout_9.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.pushButton_guardarLocalidad)
        self.pushButton_actualizarLocalidad = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_actualizarLocalidad.setObjectName("pushButton_actualizarLocalidad")
        self.formLayout_9.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.pushButton_actualizarLocalidad)
        self.frame_14 = QtWidgets.QFrame(self.tab_agregar_modificar_localidad)
        self.frame_14.setGeometry(QtCore.QRect(140, 60, 841, 80))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_buscar_categoria_por_id_2 = QtWidgets.QLabel(self.frame_14)
        self.label_buscar_categoria_por_id_2.setGeometry(QtCore.QRect(20, 20, 64, 28))
        self.label_buscar_categoria_por_id_2.setObjectName("label_buscar_categoria_por_id_2")
        self.lineEdit_buscar_localidad_por_id = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_buscar_localidad_por_id.setGeometry(QtCore.QRect(70, 20, 511, 28))
        self.lineEdit_buscar_localidad_por_id.setObjectName("lineEdit_buscar_localidad_por_id")
        self.pushButton_cargar_localidad_desde_id = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_cargar_localidad_desde_id.setGeometry(QtCore.QRect(630, 20, 191, 28))
        self.pushButton_cargar_localidad_desde_id.setObjectName("pushButton_cargar_localidad_desde_id")
        self.tabWidgetLocalidad.addTab(self.tab_agregar_modificar_localidad, "")
        self.tab_eliminar_localidad = QtWidgets.QWidget()
        self.tab_eliminar_localidad.setObjectName("tab_eliminar_localidad")
        self.frame_15 = QtWidgets.QFrame(self.tab_eliminar_localidad)
        self.frame_15.setGeometry(QtCore.QRect(60, 30, 841, 521))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.formLayout_10 = QtWidgets.QFormLayout(self.frame_15)
        self.formLayout_10.setObjectName("formLayout_10")
        self.pushButton_eliminarLocalidad = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_eliminarLocalidad.setObjectName("pushButton_eliminarLocalidad")
        self.formLayout_10.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_eliminarLocalidad)
        self.lineEdit_eliminar_idLocalidad = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_eliminar_idLocalidad.setObjectName("lineEdit_eliminar_idLocalidad")
        self.formLayout_10.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eliminar_idLocalidad)
        self.label_eliminar_idLocalidad = QtWidgets.QLabel(self.frame_15)
        self.label_eliminar_idLocalidad.setObjectName("label_eliminar_idLocalidad")
        self.formLayout_10.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_eliminar_idLocalidad)
        self.tabWidgetLocalidad.addTab(self.tab_eliminar_localidad, "")
        self.tabWidgetAplicacion.addTab(self.tab_localidades, "")
        self.tab_bancos = QtWidgets.QWidget()
        self.tab_bancos.setObjectName("tab_bancos")
        self.tabWidgetLocalidad_2 = QtWidgets.QTabWidget(self.tab_bancos)
        self.tabWidgetLocalidad_2.setGeometry(QtCore.QRect(0, 0, 1211, 751))
        self.tabWidgetLocalidad_2.setObjectName("tabWidgetLocalidad_2")
        self.tab_listado_banco = QtWidgets.QWidget()
        self.tab_listado_banco.setObjectName("tab_listado_banco")
        self.tableListaBanco = QtWidgets.QTableWidget(self.tab_listado_banco)
        self.tableListaBanco.setEnabled(True)
        self.tableListaBanco.setGeometry(QtCore.QRect(140, 200, 1021, 491))
        self.tableListaBanco.setAcceptDrops(False)
        self.tableListaBanco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaBanco.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaBanco.setLineWidth(1)
        self.tableListaBanco.setMidLineWidth(0)
        self.tableListaBanco.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaBanco.setShowGrid(True)
        self.tableListaBanco.setWordWrap(True)
        self.tableListaBanco.setCornerButtonEnabled(True)
        self.tableListaBanco.setRowCount(20)
        self.tableListaBanco.setColumnCount(3)
        self.tableListaBanco.setObjectName("tableListaBanco")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaBanco.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaBanco.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaBanco.setHorizontalHeaderItem(2, item)
        self.tableListaBanco.horizontalHeader().setCascadingSectionResizes(False)
        self.frame_buscar_banco = QtWidgets.QFrame(self.tab_listado_banco)
        self.frame_buscar_banco.setGeometry(QtCore.QRect(110, 10, 811, 111))
        self.frame_buscar_banco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_banco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_banco.setObjectName("frame_buscar_banco")
        self.btn_buscar_banco = QtWidgets.QPushButton(self.frame_buscar_banco)
        self.btn_buscar_banco.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_banco.setObjectName("btn_buscar_banco")
        self.lineEdit_buscar_banco = QtWidgets.QLineEdit(self.frame_buscar_banco)
        self.lineEdit_buscar_banco.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_banco.setObjectName("lineEdit_buscar_banco")
        self.btn_mostrar_todos_banco = QtWidgets.QPushButton(self.tab_listado_banco)
        self.btn_mostrar_todos_banco.setGeometry(QtCore.QRect(300, 140, 552, 28))
        self.btn_mostrar_todos_banco.setObjectName("btn_mostrar_todos_banco")
        self.tabWidgetLocalidad_2.addTab(self.tab_listado_banco, "")
        self.tab_agregar_modificar_banco = QtWidgets.QWidget()
        self.tab_agregar_modificar_banco.setObjectName("tab_agregar_modificar_banco")
        self.frame_16 = QtWidgets.QFrame(self.tab_agregar_modificar_banco)
        self.frame_16.setGeometry(QtCore.QRect(140, 190, 841, 291))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.formLayout_11 = QtWidgets.QFormLayout(self.frame_16)
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_nombreBanco = QtWidgets.QLabel(self.frame_16)
        self.label_nombreBanco.setObjectName("label_nombreBanco")
        self.formLayout_11.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_nombreBanco)
        self.lineEdit_nombreBanco2 = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_nombreBanco2.setObjectName("lineEdit_nombreBanco2")
        self.formLayout_11.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombreBanco2)
        self.label_observacionesBanco = QtWidgets.QLabel(self.frame_16)
        self.label_observacionesBanco.setObjectName("label_observacionesBanco")
        self.formLayout_11.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_observacionesBanco)
        self.lineEdit_observacionesBanco = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_observacionesBanco.setObjectName("lineEdit_observacionesBanco")
        self.formLayout_11.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_observacionesBanco)
        self.pushButton_guardarBanco = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_guardarBanco.setObjectName("pushButton_guardarBanco")
        self.formLayout_11.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.pushButton_guardarBanco)
        self.pushButton_actualizarBanco = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_actualizarBanco.setObjectName("pushButton_actualizarBanco")
        self.formLayout_11.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.pushButton_actualizarBanco)
        self.frame_17 = QtWidgets.QFrame(self.tab_agregar_modificar_banco)
        self.frame_17.setGeometry(QtCore.QRect(140, 60, 841, 80))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_buscar_banco_por_id = QtWidgets.QLabel(self.frame_17)
        self.label_buscar_banco_por_id.setGeometry(QtCore.QRect(20, 20, 64, 28))
        self.label_buscar_banco_por_id.setObjectName("label_buscar_banco_por_id")
        self.lineEdit_buscar_banco_por_id = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_buscar_banco_por_id.setGeometry(QtCore.QRect(70, 20, 511, 28))
        self.lineEdit_buscar_banco_por_id.setObjectName("lineEdit_buscar_banco_por_id")
        self.pushButton_cargar_banco_desde_id = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_cargar_banco_desde_id.setGeometry(QtCore.QRect(630, 20, 191, 28))
        self.pushButton_cargar_banco_desde_id.setObjectName("pushButton_cargar_banco_desde_id")
        self.tabWidgetLocalidad_2.addTab(self.tab_agregar_modificar_banco, "")
        self.tab_eliminar_banco = QtWidgets.QWidget()
        self.tab_eliminar_banco.setObjectName("tab_eliminar_banco")
        self.frame_18 = QtWidgets.QFrame(self.tab_eliminar_banco)
        self.frame_18.setGeometry(QtCore.QRect(60, 30, 841, 521))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.formLayout_12 = QtWidgets.QFormLayout(self.frame_18)
        self.formLayout_12.setObjectName("formLayout_12")
        self.pushButton_eliminarBanco = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_eliminarBanco.setObjectName("pushButton_eliminarBanco")
        self.formLayout_12.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.pushButton_eliminarBanco)
        self.lineEdit_eliminar_idBanco = QtWidgets.QLineEdit(self.frame_18)
        self.lineEdit_eliminar_idBanco.setObjectName("lineEdit_eliminar_idBanco")
        self.formLayout_12.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eliminar_idBanco)
        self.label_eliminar_idBanco = QtWidgets.QLabel(self.frame_18)
        self.label_eliminar_idBanco.setObjectName("label_eliminar_idBanco")
        self.formLayout_12.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_eliminar_idBanco)
        self.tabWidgetLocalidad_2.addTab(self.tab_eliminar_banco, "")
        self.tabWidgetAplicacion.addTab(self.tab_bancos, "")
        self.tab_detalle_venta = QtWidgets.QWidget()
        self.tab_detalle_venta.setObjectName("tab_detalle_venta")
        self.tabWidgetDetalleVenta = QtWidgets.QTabWidget(self.tab_detalle_venta)
        self.tabWidgetDetalleVenta.setGeometry(QtCore.QRect(0, 0, 1221, 761))
        self.tabWidgetDetalleVenta.setObjectName("tabWidgetDetalleVenta")
        self.tab_agregar_detalle_venta = QtWidgets.QWidget()
        self.tab_agregar_detalle_venta.setObjectName("tab_agregar_detalle_venta")
        self.tableLista_detalle_venta = QtWidgets.QTableWidget(self.tab_agregar_detalle_venta)
        self.tableLista_detalle_venta.setEnabled(True)
        self.tableLista_detalle_venta.setGeometry(QtCore.QRect(150, 280, 891, 341))
        self.tableLista_detalle_venta.setAcceptDrops(False)
        self.tableLista_detalle_venta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableLista_detalle_venta.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableLista_detalle_venta.setLineWidth(1)
        self.tableLista_detalle_venta.setMidLineWidth(0)
        self.tableLista_detalle_venta.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableLista_detalle_venta.setShowGrid(True)
        self.tableLista_detalle_venta.setWordWrap(True)
        self.tableLista_detalle_venta.setCornerButtonEnabled(True)
        self.tableLista_detalle_venta.setRowCount(20)
        self.tableLista_detalle_venta.setColumnCount(4)
        self.tableLista_detalle_venta.setObjectName("tableLista_detalle_venta")
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_venta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_venta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_venta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_venta.setHorizontalHeaderItem(3, item)
        self.tableLista_detalle_venta.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton_guardar_detalle_venta = QtWidgets.QPushButton(self.tab_agregar_detalle_venta)
        self.pushButton_guardar_detalle_venta.setGeometry(QtCore.QRect(190, 640, 833, 26))
        self.pushButton_guardar_detalle_venta.setObjectName("pushButton_guardar_detalle_venta")
        self.frame_24 = QtWidgets.QFrame(self.tab_agregar_detalle_venta)
        self.frame_24.setGeometry(QtCore.QRect(160, 20, 851, 231))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.lineEdit_cantidad_detalle_venta = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_cantidad_detalle_venta.setGeometry(QtCore.QRect(210, 110, 461, 21))
        self.lineEdit_cantidad_detalle_venta.setObjectName("lineEdit_cantidad_detalle_venta")
        self.label_cantidad_detalle_venta = QtWidgets.QLabel(self.frame_24)
        self.label_cantidad_detalle_venta.setGeometry(QtCore.QRect(80, 110, 70, 26))
        self.label_cantidad_detalle_venta.setObjectName("label_cantidad_detalle_venta")
        self.lineEdit_producto_detalle_venta = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_producto_detalle_venta.setGeometry(QtCore.QRect(210, 80, 461, 21))
        self.lineEdit_producto_detalle_venta.setObjectName("lineEdit_producto_detalle_venta")
        self.label_producto_detalle_venta = QtWidgets.QLabel(self.frame_24)
        self.label_producto_detalle_venta.setGeometry(QtCore.QRect(80, 80, 72, 28))
        self.label_producto_detalle_venta.setObjectName("label_producto_detalle_venta")
        self.lineEdit_precio_detalle_venta = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_precio_detalle_venta.setGeometry(QtCore.QRect(210, 150, 461, 21))
        self.lineEdit_precio_detalle_venta.setObjectName("lineEdit_precio_detalle_venta")
        self.label_precio_detalle_venta = QtWidgets.QLabel(self.frame_24)
        self.label_precio_detalle_venta.setGeometry(QtCore.QRect(80, 140, 49, 28))
        self.label_precio_detalle_venta.setObjectName("label_precio_detalle_venta")
        self.pushButton_agregar_detalle_venta = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_agregar_detalle_venta.setGeometry(QtCore.QRect(260, 190, 325, 28))
        self.pushButton_agregar_detalle_venta.setObjectName("pushButton_agregar_detalle_venta")
        self.lineEdit_cliente_detalle_venta = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_cliente_detalle_venta.setGeometry(QtCore.QRect(210, 20, 461, 21))
        self.lineEdit_cliente_detalle_venta.setObjectName("lineEdit_cliente_detalle_venta")
        self.label_cliente_detalle_venta = QtWidgets.QLabel(self.frame_24)
        self.label_cliente_detalle_venta.setGeometry(QtCore.QRect(80, 20, 72, 28))
        self.label_cliente_detalle_venta.setObjectName("label_cliente_detalle_venta")
        self.lineEdit_forma_pago_detalle_venta = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_forma_pago_detalle_venta.setGeometry(QtCore.QRect(210, 50, 461, 21))
        self.lineEdit_forma_pago_detalle_venta.setObjectName("lineEdit_forma_pago_detalle_venta")
        self.label_forma_pago_detalle_venta = QtWidgets.QLabel(self.frame_24)
        self.label_forma_pago_detalle_venta.setGeometry(QtCore.QRect(80, 50, 121, 28))
        self.label_forma_pago_detalle_venta.setObjectName("label_forma_pago_detalle_venta")
        self.tabWidgetDetalleVenta.addTab(self.tab_agregar_detalle_venta, "")
        self.tabWidgetAplicacion.addTab(self.tab_detalle_venta, "")
        self.tab_ventas = QtWidgets.QWidget()
        self.tab_ventas.setObjectName("tab_ventas")
        self.tabWidgetVenta = QtWidgets.QTabWidget(self.tab_ventas)
        self.tabWidgetVenta.setGeometry(QtCore.QRect(0, 0, 1221, 761))
        self.tabWidgetVenta.setObjectName("tabWidgetVenta")
        self.tab_venta = QtWidgets.QWidget()
        self.tab_venta.setObjectName("tab_venta")
        self.frame_buscar_venta = QtWidgets.QFrame(self.tab_venta)
        self.frame_buscar_venta.setGeometry(QtCore.QRect(130, 30, 811, 111))
        self.frame_buscar_venta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_venta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_venta.setObjectName("frame_buscar_venta")
        self.btn_buscar_venta = QtWidgets.QPushButton(self.frame_buscar_venta)
        self.btn_buscar_venta.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_venta.setObjectName("btn_buscar_venta")
        self.lineEdit_buscar_venta = QtWidgets.QLineEdit(self.frame_buscar_venta)
        self.lineEdit_buscar_venta.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_venta.setObjectName("lineEdit_buscar_venta")
        self.comboBox_atributo_busqueda_venta = QtWidgets.QComboBox(self.frame_buscar_venta)
        self.comboBox_atributo_busqueda_venta.setGeometry(QtCore.QRect(60, 30, 106, 28))
        self.comboBox_atributo_busqueda_venta.setObjectName("comboBox_atributo_busqueda_venta")
        self.comboBox_atributo_busqueda_venta.addItem("")
        self.comboBox_atributo_busqueda_venta.addItem("")
        self.btn_mostrar_todas_ventas = QtWidgets.QPushButton(self.tab_venta)
        self.btn_mostrar_todas_ventas.setGeometry(QtCore.QRect(320, 160, 552, 28))
        self.btn_mostrar_todas_ventas.setObjectName("btn_mostrar_todas_ventas")
        self.tableListaVenta = QtWidgets.QTableWidget(self.tab_venta)
        self.tableListaVenta.setEnabled(True)
        self.tableListaVenta.setGeometry(QtCore.QRect(60, 220, 1021, 491))
        self.tableListaVenta.setAcceptDrops(False)
        self.tableListaVenta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaVenta.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaVenta.setLineWidth(1)
        self.tableListaVenta.setMidLineWidth(0)
        self.tableListaVenta.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaVenta.setShowGrid(True)
        self.tableListaVenta.setWordWrap(True)
        self.tableListaVenta.setCornerButtonEnabled(True)
        self.tableListaVenta.setRowCount(20)
        self.tableListaVenta.setColumnCount(5)
        self.tableListaVenta.setObjectName("tableListaVenta")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaVenta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaVenta.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaVenta.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaVenta.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaVenta.setHorizontalHeaderItem(4, item)
        self.tableListaVenta.horizontalHeader().setCascadingSectionResizes(False)
        self.tabWidgetVenta.addTab(self.tab_venta, "")
        self.tabWidgetAplicacion.addTab(self.tab_ventas, "")
        self.tab_detalle_compra = QtWidgets.QWidget()
        self.tab_detalle_compra.setObjectName("tab_detalle_compra")
        self.tabWidgetDetalleCompra = QtWidgets.QTabWidget(self.tab_detalle_compra)
        self.tabWidgetDetalleCompra.setGeometry(QtCore.QRect(-10, 0, 1221, 761))
        self.tabWidgetDetalleCompra.setObjectName("tabWidgetDetalleCompra")
        self.tab_agregar_detalle_compra = QtWidgets.QWidget()
        self.tab_agregar_detalle_compra.setObjectName("tab_agregar_detalle_compra")
        self.frame_23 = QtWidgets.QFrame(self.tab_agregar_detalle_compra)
        self.frame_23.setEnabled(True)
        self.frame_23.setGeometry(QtCore.QRect(150, 10, 821, 261))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.formLayout_16 = QtWidgets.QFormLayout(self.frame_23)
        self.formLayout_16.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout_16.setObjectName("formLayout_16")
        self.label_cliente_detalle_compra = QtWidgets.QLabel(self.frame_23)
        self.label_cliente_detalle_compra.setObjectName("label_cliente_detalle_compra")
        self.formLayout_16.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_cliente_detalle_compra)
        self.lineEdit_proveedor_detalle_compra = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_proveedor_detalle_compra.setObjectName("lineEdit_proveedor_detalle_compra")
        self.formLayout_16.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_proveedor_detalle_compra)
        self.label_forma_pago_detalle_compra = QtWidgets.QLabel(self.frame_23)
        self.label_forma_pago_detalle_compra.setObjectName("label_forma_pago_detalle_compra")
        self.formLayout_16.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_forma_pago_detalle_compra)
        self.label_producto_detalle_compra = QtWidgets.QLabel(self.frame_23)
        self.label_producto_detalle_compra.setObjectName("label_producto_detalle_compra")
        self.formLayout_16.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_producto_detalle_compra)
        self.label_cantidad_detalle_compra = QtWidgets.QLabel(self.frame_23)
        self.label_cantidad_detalle_compra.setObjectName("label_cantidad_detalle_compra")
        self.formLayout_16.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_cantidad_detalle_compra)
        self.lineEdit_cantidad_detalle_compra = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_cantidad_detalle_compra.setObjectName("lineEdit_cantidad_detalle_compra")
        self.formLayout_16.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_cantidad_detalle_compra)
        self.label_precio_detalle_compra = QtWidgets.QLabel(self.frame_23)
        self.label_precio_detalle_compra.setObjectName("label_precio_detalle_compra")
        self.formLayout_16.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_precio_detalle_compra)
        self.lineEdit_precio_detalle_compra = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_precio_detalle_compra.setObjectName("lineEdit_precio_detalle_compra")
        self.formLayout_16.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_precio_detalle_compra)
        self.pushButton_agregar_detalle_compra = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_agregar_detalle_compra.setObjectName("pushButton_agregar_detalle_compra")
        self.formLayout_16.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.pushButton_agregar_detalle_compra)
        self.lineEdit_producto_detalle_compra = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_producto_detalle_compra.setObjectName("lineEdit_producto_detalle_compra")
        self.formLayout_16.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_producto_detalle_compra)
        self.lineEdit_forma_pago_detalle_compra = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_forma_pago_detalle_compra.setObjectName("lineEdit_forma_pago_detalle_compra")
        self.formLayout_16.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_forma_pago_detalle_compra)
        self.tableLista_detalle_compra = QtWidgets.QTableWidget(self.tab_agregar_detalle_compra)
        self.tableLista_detalle_compra.setEnabled(True)
        self.tableLista_detalle_compra.setGeometry(QtCore.QRect(150, 280, 891, 341))
        self.tableLista_detalle_compra.setAcceptDrops(False)
        self.tableLista_detalle_compra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableLista_detalle_compra.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableLista_detalle_compra.setLineWidth(1)
        self.tableLista_detalle_compra.setMidLineWidth(0)
        self.tableLista_detalle_compra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableLista_detalle_compra.setShowGrid(True)
        self.tableLista_detalle_compra.setWordWrap(True)
        self.tableLista_detalle_compra.setCornerButtonEnabled(True)
        self.tableLista_detalle_compra.setRowCount(20)
        self.tableLista_detalle_compra.setColumnCount(4)
        self.tableLista_detalle_compra.setObjectName("tableLista_detalle_compra")
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_compra.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_compra.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_compra.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLista_detalle_compra.setHorizontalHeaderItem(3, item)
        self.tableLista_detalle_compra.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton_guardar_detalle_compra = QtWidgets.QPushButton(self.tab_agregar_detalle_compra)
        self.pushButton_guardar_detalle_compra.setGeometry(QtCore.QRect(190, 640, 833, 26))
        self.pushButton_guardar_detalle_compra.setObjectName("pushButton_guardar_detalle_compra")
        self.tabWidgetDetalleCompra.addTab(self.tab_agregar_detalle_compra, "")
        self.tabWidgetAplicacion.addTab(self.tab_detalle_compra, "")
        self.tab_compras = QtWidgets.QWidget()
        self.tab_compras.setObjectName("tab_compras")
        self.tabWidgetCompra = QtWidgets.QTabWidget(self.tab_compras)
        self.tabWidgetCompra.setGeometry(QtCore.QRect(-10, 0, 1221, 761))
        self.tabWidgetCompra.setObjectName("tabWidgetCompra")
        self.tab_compra = QtWidgets.QWidget()
        self.tab_compra.setObjectName("tab_compra")
        self.frame_buscar_compra = QtWidgets.QFrame(self.tab_compra)
        self.frame_buscar_compra.setGeometry(QtCore.QRect(130, 30, 811, 111))
        self.frame_buscar_compra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buscar_compra.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buscar_compra.setObjectName("frame_buscar_compra")
        self.btn_buscar_compra = QtWidgets.QPushButton(self.frame_buscar_compra)
        self.btn_buscar_compra.setGeometry(QtCore.QRect(189, 64, 552, 28))
        self.btn_buscar_compra.setObjectName("btn_buscar_compra")
        self.lineEdit_buscar_compra = QtWidgets.QLineEdit(self.frame_buscar_compra)
        self.lineEdit_buscar_compra.setGeometry(QtCore.QRect(189, 30, 552, 28))
        self.lineEdit_buscar_compra.setObjectName("lineEdit_buscar_compra")
        self.comboBox_atributo_busqueda_compra = QtWidgets.QComboBox(self.frame_buscar_compra)
        self.comboBox_atributo_busqueda_compra.setGeometry(QtCore.QRect(60, 30, 106, 28))
        self.comboBox_atributo_busqueda_compra.setObjectName("comboBox_atributo_busqueda_compra")
        self.comboBox_atributo_busqueda_compra.addItem("")
        self.comboBox_atributo_busqueda_compra.addItem("")
        self.btn_mostrar_todas_compras = QtWidgets.QPushButton(self.tab_compra)
        self.btn_mostrar_todas_compras.setGeometry(QtCore.QRect(320, 160, 552, 28))
        self.btn_mostrar_todas_compras.setObjectName("btn_mostrar_todas_compras")
        self.tableListaCompra = QtWidgets.QTableWidget(self.tab_compra)
        self.tableListaCompra.setEnabled(True)
        self.tableListaCompra.setGeometry(QtCore.QRect(60, 220, 1021, 491))
        self.tableListaCompra.setAcceptDrops(False)
        self.tableListaCompra.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableListaCompra.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableListaCompra.setLineWidth(1)
        self.tableListaCompra.setMidLineWidth(0)
        self.tableListaCompra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableListaCompra.setShowGrid(True)
        self.tableListaCompra.setWordWrap(True)
        self.tableListaCompra.setCornerButtonEnabled(True)
        self.tableListaCompra.setRowCount(20)
        self.tableListaCompra.setColumnCount(5)
        self.tableListaCompra.setObjectName("tableListaCompra")
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCompra.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCompra.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCompra.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCompra.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableListaCompra.setHorizontalHeaderItem(4, item)
        self.tableListaCompra.horizontalHeader().setCascadingSectionResizes(False)
        self.tabWidgetCompra.addTab(self.tab_compra, "")
        self.tabWidgetAplicacion.addTab(self.tab_compras, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1259, 25))
        self.menubar.setObjectName("menubar")
        self.acercaDe = QtWidgets.QMenu(self.menubar)
        self.acercaDe.setObjectName("acercaDe")
        MainWindow.setMenuBar(self.menubar)
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.acercaDe.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.acercaDe.menuAction())

        self.retranslateUi(MainWindow, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria,
                           servicio_localidad, servicio_banco, servicio_detalle_venta, servicio_venta)
        self.tabWidgetAplicacion.setCurrentIndex(0)
        self.tabWidgetProducto.setCurrentIndex(0)
        self.tabWidgetCliente.setCurrentIndex(0)
        self.tabWidgetProveedor.setCurrentIndex(0)
        self.tabWidgetCliente_2.setCurrentIndex(0)
        self.tabWidgetLocalidad.setCurrentIndex(0)
        self.tabWidgetLocalidad_2.setCurrentIndex(0)
        self.tabWidgetDetalleVenta.setCurrentIndex(0)
        self.tabWidgetVenta.setCurrentIndex(0)
        self.tabWidgetDetalleCompra.setCurrentIndex(0)
        self.tabWidgetCompra.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, servicio_producto, servicio_cliente, servicio_proveedor, servicio_categoria,
                      servicio_localidad, servicio_banco, servicio_detalle_venta, servicio_venta):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_atributo_busqueda_producto.setItemText(0, _translate("MainWindow", "Nombre"))
        self.comboBox_atributo_busqueda_producto.setItemText(1, _translate("MainWindow", "Marca"))
        self.comboBox_atributo_busqueda_producto.setItemText(2, _translate("MainWindow", "Categoria"))
        self.comboBox_atributo_busqueda_producto.setItemText(3, _translate("MainWindow", "Proveedor"))
        self.btn_buscar_producto.setText(_translate("MainWindow", "Buscar"))
        self.tableResultadoBusquedaProducto.setSortingEnabled(False)
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id producto"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio unitario"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Unidades en stock"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.tableResultadoBusquedaProducto.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Observaciones"))
        self.btn_mostrar_todos_productos.setText(_translate("MainWindow", "Mostrar todos"))
        self.tabWidgetProducto.setTabText(self.tabWidgetProducto.indexOf(self.tab_listado_producto),
                                          _translate("MainWindow", "Listado productos"))
        self.label_agregar_producto_nombre.setText(_translate("MainWindow", "Nombre"))
        self.label_agregar_producto_marca.setText(_translate("MainWindow", "Marca"))
        self.label_agregar_producto_categoria.setText(_translate("MainWindow", "Categoria"))
        self.label_agregar_producto_precio_unitario.setText(_translate("MainWindow", "Precio unitario"))
        self.label_agregar_producto_precio_unitario_2.setText(_translate("MainWindow", "Unidades en stock"))
        self.label_agregar_producto_proveedor.setText(_translate("MainWindow", "Proveedor"))
        self.label_agregar_producto_descripcion.setText(_translate("MainWindow", "Descripcion"))
        self.label_agregar_producto_observaciones.setText(_translate("MainWindow", "Observaciones"))
        self.pushButton_agregar_producto_guardar.setText(_translate("MainWindow", "Guardar"))
        self.pushButton_actualizar_producto.setText(_translate("MainWindow", "Actualizar"))
        self.label_buscar_producto_por_id.setText(_translate("MainWindow", "ID"))
        self.pushButton_cargar_producto_desde_id.setText(_translate("MainWindow", "Cargar"))
        self.tabWidgetProducto.setTabText(self.tabWidgetProducto.indexOf(self.tab_agregar_modificar_producto),
                                          _translate("MainWindow", "Agregar/Modificar producto"))
        self.pushButton_eliminarProducto.setText(_translate("MainWindow", "Borrar"))
        self.label_eliminar_idProducto.setText(_translate("MainWindow", "ID producto"))
        self.tabWidgetProducto.setTabText(self.tabWidgetProducto.indexOf(self.tab_eliminar_producto),
                                          _translate("MainWindow", "Eliminar producto"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_producto),
                                            _translate("MainWindow", "Productos"))
        self.tableListaCliente.setSortingEnabled(False)
        item = self.tableListaCliente.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id cliente"))
        item = self.tableListaCliente.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableListaCliente.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableListaCliente.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.tableListaCliente.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.tableListaCliente.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tableListaCliente.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tableListaCliente.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Observaciones"))
        self.comboBox_atributo_busqueda_cliente.setItemText(0, _translate("MainWindow", "Nombre"))
        self.comboBox_atributo_busqueda_cliente.setItemText(1, _translate("MainWindow", "Apellido"))
        self.comboBox_atributo_busqueda_cliente.setItemText(2, _translate("MainWindow", "Localidad"))
        self.comboBox_atributo_busqueda_cliente.setItemText(3, _translate("MainWindow", "Provincia"))
        self.btn_buscar_cliente.setText(_translate("MainWindow", "Buscar"))
        self.btn_mostrar_todos_clientes.setText(_translate("MainWindow", "Mostrar todos"))
        self.tabWidgetCliente.setTabText(self.tabWidgetCliente.indexOf(self.tab_listado_cliente),
                                         _translate("MainWindow", "Listado clientes"))
        self.label_nombreCliente.setText(_translate("MainWindow", "Nombre"))
        self.label_apellidoCliente.setText(_translate("MainWindow", "Apellido"))
        self.label_direccionCliente.setText(_translate("MainWindow", "Direccion"))
        self.label_localidadCliente.setText(_translate("MainWindow", "Localidad"))
        self.label_telefonoCliente.setText(_translate("MainWindow", "Telefono"))
        self.label_dniCliente.setText(_translate("MainWindow", "DNI"))
        self.label_observacionesCliente.setText(_translate("MainWindow", "Observaciones"))
        self.pushButton_guardarCliente.setText(_translate("MainWindow", "Guardar"))
        self.pushButton_actualizarCliente.setText(_translate("MainWindow", "Actualizar"))
        self.label_buscar_cliente_por_id.setText(_translate("MainWindow", "ID"))
        self.pushButton_cargar_cliente_desde_id.setText(_translate("MainWindow", "Cargar"))
        self.tabWidgetCliente.setTabText(self.tabWidgetCliente.indexOf(self.tab_agregar_modificar_cliente),
                                         _translate("MainWindow", "Agregar/Modificar cliente"))
        self.pushButton_eliminarCliente.setText(_translate("MainWindow", "Borrar"))
        self.label_eliminar_idCliente.setText(_translate("MainWindow", "ID cliente"))
        self.tabWidgetCliente.setTabText(self.tabWidgetCliente.indexOf(self.tab_eliminar_cliente),
                                         _translate("MainWindow", "Eliminar cliente"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_cliente),
                                            _translate("MainWindow", "Clientes"))
        self.tableListaProveedor.setSortingEnabled(False)
        item = self.tableListaProveedor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id proveedor"))
        item = self.tableListaProveedor.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableListaProveedor.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Direccion comercial"))
        item = self.tableListaProveedor.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.tableListaProveedor.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tableListaProveedor.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableListaProveedor.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tableListaProveedor.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CBU"))
        item = self.tableListaProveedor.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Banco CBU"))
        item = self.tableListaProveedor.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "CUIT"))
        item = self.tableListaProveedor.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Categoria IVA"))
        item = self.tableListaProveedor.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Observaciones"))
        self.comboBox_atributo_busqueda_proveedor.setItemText(0, _translate("MainWindow", "Nombre"))
        self.comboBox_atributo_busqueda_proveedor.setItemText(1, _translate("MainWindow", "Localidad"))
        self.comboBox_atributo_busqueda_proveedor.setItemText(2, _translate("MainWindow", "Provincia"))
        self.btn_buscar_proveedor.setText(_translate("MainWindow", "Buscar"))
        self.btn_mostrar_todos_proveedores.setText(_translate("MainWindow", "Mostrar todos"))
        self.tabWidgetProveedor.setTabText(self.tabWidgetProveedor.indexOf(self.tab_listado_proveedor),
                                           _translate("MainWindow", "Listado proveedores"))
        self.label_nombreProveedor.setText(_translate("MainWindow", "Nombre"))
        self.label_direccionComercialProveedor.setText(_translate("MainWindow", "Direccion comercial"))
        self.label_localidadProveedor.setText(_translate("MainWindow", "Localidad"))
        self.label_telefonoProveedor.setText(_translate("MainWindow", "Telefono"))
        self.label_emailProveedor.setText(_translate("MainWindow", "Email"))
        self.label_dniProveedor.setText(_translate("MainWindow", "DNI"))
        self.label_cbuProveedor.setText(_translate("MainWindow", "CBU"))
        self.label_bancoCbuProveedor.setText(_translate("MainWindow", "Banco CBU"))
        self.label_cuitProveedor.setText(_translate("MainWindow", "CUIT"))
        self.label_categoriaIvaProveedor.setText(_translate("MainWindow", "Categoria IVA"))
        self.label_observacionesProveedor.setText(_translate("MainWindow", "Observaciones"))
        self.pushButton_guardarProveedor.setText(_translate("MainWindow", "Guardar"))
        self.pushButton_actualizarProveedor.setText(_translate("MainWindow", "Actualizar"))
        self.label_buscar_proveedor_por_id.setText(_translate("MainWindow", "ID"))
        self.pushButton_cargar_proveedor_desde_id.setText(_translate("MainWindow", "Cargar"))
        self.tabWidgetProveedor.setTabText(self.tabWidgetProveedor.indexOf(self.tab_agregar_modificar_proveedor),
                                           _translate("MainWindow", "Agregar/Modificar proveedor"))
        self.pushButton_eliminarProveedor.setText(_translate("MainWindow", "Borrar"))
        self.label_eliminar_idProveedor.setText(_translate("MainWindow", "ID proveedor"))
        self.tabWidgetProveedor.setTabText(self.tabWidgetProveedor.indexOf(self.tab_eliminar_proveedor),
                                           _translate("MainWindow", "Eliminar proveedor"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_proveedor),
                                            _translate("MainWindow", "Proveedores"))
        self.tableListaCategoria.setSortingEnabled(False)
        item = self.tableListaCategoria.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id categoria"))
        item = self.tableListaCategoria.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableListaCategoria.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Observaciones"))
        self.btn_buscar_categoria.setText(_translate("MainWindow", "Buscar"))
        self.btn_mostrar_todos_categorias.setText(_translate("MainWindow", "Mostrar todos"))
        self.tabWidgetCliente_2.setTabText(self.tabWidgetCliente_2.indexOf(self.tab_listado_categoria),
                                           _translate("MainWindow", "Listado categorias"))
        self.label_nombreCategoria.setText(_translate("MainWindow", "Nombre"))
        self.label_observacionesCategoria.setText(_translate("MainWindow", "Observaciones"))
        self.pushButton_guardarCategoria.setText(_translate("MainWindow", "Guardar"))
        self.pushButton_actualizarCategoria.setText(_translate("MainWindow", "Actualizar"))
        self.label_buscar_categoria_por_id.setText(_translate("MainWindow", "ID"))
        self.pushButton_cargar_categoria_desde_id.setText(_translate("MainWindow", "Cargar"))
        self.tabWidgetCliente_2.setTabText(self.tabWidgetCliente_2.indexOf(self.tab_agregar_modificar_categoria),
                                           _translate("MainWindow", "Agregar/Modificar categoria"))
        self.pushButton_eliminarCategoria.setText(_translate("MainWindow", "Borrar"))
        self.label_eliminar_idCategoria.setText(_translate("MainWindow", "ID categoria"))
        self.tabWidgetCliente_2.setTabText(self.tabWidgetCliente_2.indexOf(self.tab_eliminar_categoria),
                                           _translate("MainWindow", "Eliminar categoria"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_categoria),
                                            _translate("MainWindow", "Categorias"))
        self.tableListaLocalidad.setSortingEnabled(False)
        item = self.tableListaLocalidad.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id Localidad"))
        item = self.tableListaLocalidad.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableListaLocalidad.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Codigo postal"))
        item = self.tableListaLocalidad.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Provincia"))
        self.btn_buscar_localidad.setText(_translate("MainWindow", "Buscar"))
        self.comboBox_atributo_busqueda_cliente_2.setItemText(0, _translate("MainWindow", "Nombre"))
        self.comboBox_atributo_busqueda_cliente_2.setItemText(1, _translate("MainWindow", "Codigo postal"))
        self.comboBox_atributo_busqueda_cliente_2.setItemText(2, _translate("MainWindow", "Provincia"))
        self.btn_mostrar_todos_localidad.setText(_translate("MainWindow", "Mostrar todos"))
        self.tabWidgetLocalidad.setTabText(self.tabWidgetLocalidad.indexOf(self.tab_listado_localidad),
                                           _translate("MainWindow", "Listado localidades"))
        self.label_nombreLocalidad.setText(_translate("MainWindow", "Nombre"))
        self.label_codigo_postal_Localidad.setText(_translate("MainWindow", "Codigo postal"))
        self.label_provinciaLocalidad.setText(_translate("MainWindow", "Provincia"))
        self.pushButton_guardarLocalidad.setText(_translate("MainWindow", "Guardar"))
        self.pushButton_actualizarLocalidad.setText(_translate("MainWindow", "Actualizar"))
        self.label_buscar_categoria_por_id_2.setText(_translate("MainWindow", "ID"))
        self.pushButton_cargar_localidad_desde_id.setText(_translate("MainWindow", "Cargar"))
        self.tabWidgetLocalidad.setTabText(self.tabWidgetLocalidad.indexOf(self.tab_agregar_modificar_localidad),
                                           _translate("MainWindow", "Agregar/Modificar localidad"))
        self.pushButton_eliminarLocalidad.setText(_translate("MainWindow", "Borrar"))
        self.label_eliminar_idLocalidad.setText(_translate("MainWindow", "ID localidad"))
        self.tabWidgetLocalidad.setTabText(self.tabWidgetLocalidad.indexOf(self.tab_eliminar_localidad),
                                           _translate("MainWindow", "Eliminar localidad"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_localidades),
                                            _translate("MainWindow", "Localidades"))
        self.tableListaBanco.setSortingEnabled(False)
        item = self.tableListaBanco.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id Banco"))
        item = self.tableListaBanco.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableListaBanco.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Observaciones"))
        self.btn_buscar_banco.setText(_translate("MainWindow", "Buscar"))
        self.btn_mostrar_todos_banco.setText(_translate("MainWindow", "Mostrar todos"))
        self.tabWidgetLocalidad_2.setTabText(self.tabWidgetLocalidad_2.indexOf(self.tab_listado_banco),
                                             _translate("MainWindow", "Listado bancos"))
        self.label_nombreBanco.setText(_translate("MainWindow", "Nombre"))
        self.label_observacionesBanco.setText(_translate("MainWindow", "Observaciones"))
        self.pushButton_guardarBanco.setText(_translate("MainWindow", "Guardar"))
        self.pushButton_actualizarBanco.setText(_translate("MainWindow", "Actualizar"))
        self.label_buscar_banco_por_id.setText(_translate("MainWindow", "ID"))
        self.pushButton_cargar_banco_desde_id.setText(_translate("MainWindow", "Cargar"))
        self.tabWidgetLocalidad_2.setTabText(self.tabWidgetLocalidad_2.indexOf(self.tab_agregar_modificar_banco),
                                             _translate("MainWindow", "Agregar/Modificar banco"))
        self.pushButton_eliminarBanco.setText(_translate("MainWindow", "Borrar"))
        self.label_eliminar_idBanco.setText(_translate("MainWindow", "ID banco"))
        self.tabWidgetLocalidad_2.setTabText(self.tabWidgetLocalidad_2.indexOf(self.tab_eliminar_banco),
                                             _translate("MainWindow", "Eliminar banco"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_bancos),
                                            _translate("MainWindow", "Bancos"))
        self.tableLista_detalle_venta.setSortingEnabled(False)
        item = self.tableLista_detalle_venta.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.tableLista_detalle_venta.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tableLista_detalle_venta.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tableLista_detalle_venta.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total item"))
        self.pushButton_guardar_detalle_venta.setText(_translate("MainWindow", "Guardar"))
        self.label_cantidad_detalle_venta.setText(_translate("MainWindow", "Cantidad"))
        self.label_producto_detalle_venta.setText(_translate("MainWindow", "Producto"))
        self.label_precio_detalle_venta.setText(_translate("MainWindow", "Precio"))
        self.pushButton_agregar_detalle_venta.setText(_translate("MainWindow", "Agregar"))
        self.label_cliente_detalle_venta.setText(_translate("MainWindow", "Cliente"))
        self.label_forma_pago_detalle_venta.setText(_translate("MainWindow", "Forma de pago"))
        self.tabWidgetDetalleVenta.setTabText(self.tabWidgetDetalleVenta.indexOf(self.tab_agregar_detalle_venta),
                                              _translate("MainWindow", "Agregar item detalle venta"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_detalle_venta),
                                            _translate("MainWindow", "Detalle venta"))
        self.btn_buscar_venta.setText(_translate("MainWindow", "Buscar"))
        self.comboBox_atributo_busqueda_venta.setItemText(0, _translate("MainWindow", "Cliente"))
        self.comboBox_atributo_busqueda_venta.setItemText(1, _translate("MainWindow", "Fecha"))
        self.btn_mostrar_todas_ventas.setText(_translate("MainWindow", "Mostrar todos"))
        self.tableListaVenta.setSortingEnabled(False)
        item = self.tableListaVenta.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id venta"))
        item = self.tableListaVenta.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tableListaVenta.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Forma de pago"))
        item = self.tableListaVenta.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total venta"))
        item = self.tableListaVenta.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cliente"))
        self.tabWidgetVenta.setTabText(self.tabWidgetVenta.indexOf(self.tab_venta), _translate("MainWindow", "Ventas"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_ventas),
                                            _translate("MainWindow", "Ventas"))
        self.label_cliente_detalle_compra.setText(_translate("MainWindow", "Proveedor"))
        self.label_forma_pago_detalle_compra.setText(_translate("MainWindow", "Forma de pago"))
        self.label_producto_detalle_compra.setText(_translate("MainWindow", "Producto"))
        self.label_cantidad_detalle_compra.setText(_translate("MainWindow", "Cantidad"))
        self.label_precio_detalle_compra.setText(_translate("MainWindow", "Precio"))
        self.pushButton_agregar_detalle_compra.setText(_translate("MainWindow", "Agregar"))
        self.tableLista_detalle_compra.setSortingEnabled(False)
        item = self.tableLista_detalle_compra.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Producto"))
        item = self.tableLista_detalle_compra.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tableLista_detalle_compra.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tableLista_detalle_compra.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total item"))
        self.pushButton_guardar_detalle_compra.setText(_translate("MainWindow", "Guardar"))
        self.tabWidgetDetalleCompra.setTabText(self.tabWidgetDetalleCompra.indexOf(self.tab_agregar_detalle_compra),
                                               _translate("MainWindow", "Agregar item detalle compra"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_detalle_compra),
                                            _translate("MainWindow", "Detalle compra"))
        self.btn_buscar_compra.setText(_translate("MainWindow", "Buscar"))
        self.comboBox_atributo_busqueda_compra.setItemText(0, _translate("MainWindow", "Proveedor"))
        self.comboBox_atributo_busqueda_compra.setItemText(1, _translate("MainWindow", "Fecha"))
        self.btn_mostrar_todas_compras.setText(_translate("MainWindow", "Mostrar todos"))
        self.tableListaCompra.setSortingEnabled(False)
        item = self.tableListaCompra.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id compra"))
        item = self.tableListaCompra.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tableListaCompra.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Forma de pago"))
        item = self.tableListaCompra.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total compra"))
        item = self.tableListaCompra.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Proveedor"))
        self.tabWidgetCompra.setTabText(self.tabWidgetCompra.indexOf(self.tab_compra),
                                        _translate("MainWindow", "Compras"))
        self.tabWidgetAplicacion.setTabText(self.tabWidgetAplicacion.indexOf(self.tab_compras),
                                            _translate("MainWindow", "Compras"))
        self.acercaDe.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))

        # CREA CELDAS EN TABLAS
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_productoDto):
                item = QtWidgets.QTableWidgetItem()
                self.tableResultadoBusquedaProducto.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_clienteDto):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaCliente.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_proveedorDto):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaProveedor.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_categoriaDto):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaCategoria.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_localidadDto):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaLocalidad.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_bancoDto):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaBanco.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_detalle_ventas):
                item = QtWidgets.QTableWidgetItem()
                self.tableLista_detalle_venta.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_ventas):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaVenta.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_detalle_compras):
                item = QtWidgets.QTableWidgetItem()
                self.tableLista_detalle_compra.setItem(i, j, item)

        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_compras):
                item = QtWidgets.QTableWidgetItem()
                self.tableListaCompra.setItem(i, j, item)

        formulario_nuevo_producto = {"nombre": self.lineEdit_agregar_producto_nombre,
                                     "marca": self.lineEdit_agregar_producto_marca,
                                     "categoria": self.lineEdit_agregar_producto_categoria,
                                     "precio_unitario": self.lineEdit_agregar_producto_precio_unitario,
                                     "unidades_stock": self.lineEdit_agregar_producto_unidades_stock,
                                     "descripcion": self.lineEdit_agregar_producto_descripcion,
                                     "observaciones": self.lineEdit_agregar_producto_observaciones}

        formulario_nuevo_cliente = {"nombre": self.lineEdit_nombreCliente,
                                    "apellido": self.lineEdit_apellidoCliente,
                                    "direccion": self.lineEdit_direccionCliente,
                                    "localidad": self.lineEdit_localidadCliente,
                                    "telefono": self.lineEdit_telefonoCliente,
                                    "dni": self.lineEdit_dniCliente,
                                    "observaciones": self.lineEdit_observacionesCliente
                                    }

        formulario_nuevo_proveedor = {"nombre": self.lineEdit_nombreProveedor,
                                      "direccion_comercial": self.lineEdit_direccionComercialProveedor,
                                      "localidad": self.lineEdit_localidadProveedor,
                                      "telefono": self.lineEdit_telefonoProveedor,
                                      "email": self.lineEdit_emailProveedor,
                                      "dni": self.lineEdit_dniProveedor,
                                      "cbu": self.lineEdit_cbuProveedor,
                                      "banco_cbu": self.lineEdit_bancoCbuProveedor,
                                      "cuit": self.lineEdit_cuitProveedor,
                                      "categoria_iva": self.lineEdit_categoriaIvaProveedor,
                                      "observaciones": self.lineEdit_observacionesProveedor}

        formulario_nueva_categoria = {"nombre": self.lineEdit_nombreCategoria,
                                      "observaciones": self.lineEdit_observacionesCategoria}

        formulario_nueva_localidad = {"nombre": self.lineEdit_nombreLocalidad,
                                      "codigo_postal": self.lineEdit_codigo_postal_Localidad,
                                      "provincia": self.lineEdit_provinciaLocalidad}

        fomulario_nuevo_banco = {"nombre": self.lineEdit_nombreBanco2,
                                 "observaciones": self.lineEdit_observacionesBanco}

        formulario_detalle_venta = {"producto": self.lineEdit_producto_detalle_venta,
                                    "cantidad": self.lineEdit_cantidad_detalle_venta,
                                    "precio": self.lineEdit_precio_detalle_venta,
                                    "cliente": self.lineEdit_cliente_detalle_venta,
                                    "forma_pago": self.lineEdit_forma_pago_detalle_venta}

        formulario_detalle_compra = {"producto": self.lineEdit_producto_detalle_compra,
                                     "cantidad": self.lineEdit_cantidad_detalle_compra,
                                     "precio": self.lineEdit_precio_detalle_compra,
                                     "proveedor": self.lineEdit_proveedor_detalle_compra,
                                     "forma_pago": self.lineEdit_forma_pago_detalle_compra}

        # EVENT HANDLERS PARA BOTONES
        self.btn_buscar_producto.clicked.connect(
            lambda: self.busqueda_producto_handler(servicio_producto, self.comboBox_atributo_busqueda_producto,
                                                   self.lineEdit_buscar_producto,
                                                   self.tableResultadoBusquedaProducto))

        self.btn_mostrar_todos_productos.clicked.connect(
            lambda: self.mostrar_todos_productos(servicio_producto, self.tableResultadoBusquedaProducto)
        )

        self.pushButton_agregar_producto_guardar.clicked.connect(
            lambda: self.guardar_producto(servicio_producto, formulario_nuevo_producto))

        self.pushButton_eliminarProducto.clicked.connect(
            lambda: self.eliminar_producto(servicio_producto, self.lineEdit_eliminar_idProducto)
        )

        self.pushButton_cargar_producto_desde_id.clicked.connect(
            lambda: self.cargar_producto_desde_id(servicio_producto, self.lineEdit_buscar_producto_por_id,
                                                  formulario_nuevo_producto)
        )

        self.btn_mostrar_todos_clientes.clicked.connect(
            lambda: self.mostrar_todos_clientes(servicio_cliente, self.tableListaCliente)
        )

        self.pushButton_guardarCliente.clicked.connect(
            lambda: self.guardar_cliente(servicio_cliente, formulario_nuevo_cliente)
        )

        self.btn_buscar_cliente.clicked.connect(
            lambda: self.busqueda_cliente_handler(servicio_cliente, self.comboBox_atributo_busqueda_cliente,
                                                  self.lineEdit_buscar_cliente, self.tableListaCliente)
        )

        self.pushButton_cargar_cliente_desde_id.clicked.connect(
            lambda: self.cargar_cliente_desde_id(servicio_cliente, self.lineEdit_buscar_cliente_por_id,
                                                 formulario_nuevo_cliente)
        )

        self.pushButton_actualizarCliente.clicked.connect(
            lambda: self.actualizar_cliente(servicio_cliente, formulario_nuevo_cliente,
                                            self.lineEdit_buscar_cliente_por_id)
        )

        self.pushButton_eliminarCliente.clicked.connect(
            lambda: self.eliminar_cliente(servicio_cliente, self.lineEdit_eliminar_idCliente)
        )

        self.btn_mostrar_todos_proveedores.clicked.connect(
            lambda: self.mostrar_todos_proveedores(servicio_proveedor, self.tableListaProveedor)
        )

        self.btn_buscar_proveedor.clicked.connect(
            lambda: self.busqueda_proveedor_handler(servicio_proveedor, self.comboBox_atributo_busqueda_proveedor,
                                                    self.lineEdit_buscar_proveedor, self.tableListaProveedor)
        )

        self.pushButton_eliminarProveedor.clicked.connect(
            lambda: self.eliminar_proveedor(servicio_proveedor, self.lineEdit_eliminar_idProveedor)
        )

        self.pushButton_cargar_proveedor_desde_id.clicked.connect(
            lambda: self.cargar_proveedor_desde_id(servicio_proveedor, self.lineEdit_buscar_proveedor_por_id,
                                                   formulario_nuevo_proveedor)
        )

        self.pushButton_actualizarProveedor.clicked.connect(
            lambda: self.actualizar_proveedor(servicio_proveedor, formulario_nuevo_proveedor,
                                              self.lineEdit_buscar_proveedor_por_id)
        )

        self.pushButton_guardarProveedor.clicked.connect(
            lambda: self.guardar_proveedor(servicio_proveedor, formulario_nuevo_proveedor)
        )

        self.pushButton_guardarCategoria.clicked.connect(
            lambda: self.guardar_categoria(servicio_categoria, formulario_nueva_categoria)
        )

        self.btn_mostrar_todos_categorias.clicked.connect(
            lambda: self.mostrar_todas_categorias(servicio_categoria, self.tableListaCategoria)
        )

        self.btn_buscar_categoria.clicked.connect(
            lambda: self.buscar_categoria(servicio_categoria, self.lineEdit_buscar_categoria, self.tableListaCategoria)
        )

        self.pushButton_cargar_categoria_desde_id.clicked.connect(
            lambda: self.cargar_categoria_desde_id(servicio_categoria, self.lineEdit_buscar_categoria_por_id,
                                                   formulario_nueva_categoria)
        )

        self.pushButton_actualizarCategoria.clicked.connect(
            lambda: self.actualizar_categoria(servicio_categoria, formulario_nueva_categoria,
                                              self.lineEdit_buscar_categoria_por_id)
        )

        self.pushButton_eliminarCategoria.clicked.connect(
            lambda: self.eliminar_categoria(servicio_categoria, self.lineEdit_eliminar_idCategoria)
        )

        self.btn_mostrar_todos_localidad.clicked.connect(
            lambda: self.mostrar_todas_localidades(servicio_localidad, self.tableListaLocalidad)
        )

        # BUSQUEDA DE LOCALIDADES
        self.btn_buscar_localidad.clicked.connect(
            lambda: self.buscar_localidad(servicio_localidad, self.lineEdit_buscar_localidad, self.tableListaLocalidad)
        )

        self.pushButton_cargar_localidad_desde_id.clicked.connect(
            lambda: self.cargar_localidad_desde_id(servicio_localidad, self.lineEdit_buscar_localidad_por_id,
                                                   formulario_nueva_localidad)
        )

        self.pushButton_guardarLocalidad.clicked.connect(
            lambda: self.guardar_localidad(servicio_localidad, formulario_nueva_localidad)
        )

        self.pushButton_actualizarLocalidad.clicked.connect(
            lambda: self.actualizar_localidad(servicio_localidad, formulario_nueva_localidad,
                                              self.lineEdit_buscar_localidad_por_id)
        )

        self.pushButton_eliminarLocalidad.clicked.connect(
            lambda: self.eliminar_localidad(servicio_localidad, self.lineEdit_eliminar_idLocalidad)
        )

        self.btn_mostrar_todos_banco.clicked.connect(
            lambda: self.mostrar_todos_bancos(servicio_banco, self.tableListaBanco)
        )

        self.pushButton_eliminarBanco.clicked.connect(
            lambda: self.eliminar_banco(servicio_banco, self.lineEdit_eliminar_idBanco)
        )

        self.pushButton_guardarBanco.clicked.connect(
            lambda: self.guardar_banco(servicio_banco, fomulario_nuevo_banco)
        )

        self.pushButton_cargar_banco_desde_id.clicked.connect(
            lambda: self.cargar_banco_desde_id(servicio_banco, self.lineEdit_buscar_banco_por_id, fomulario_nuevo_banco)
        )

        self.pushButton_actualizarBanco.clicked.connect(
            lambda: self.actualizar_banco(servicio_banco, fomulario_nuevo_banco, self.lineEdit_buscar_banco_por_id)
        )

        self.btn_buscar_banco.clicked.connect(
            lambda: self.buscar_banco(servicio_banco, self.lineEdit_buscar_banco, self.tableListaBanco)
        )

        self.pushButton_agregar_detalle_venta.clicked.connect(
            lambda: self.agregar_detalle_venta(servicio_detalle_venta, formulario_detalle_venta,
                                               self.tableLista_detalle_venta)
        )

        self.pushButton_guardar_detalle_venta.clicked.connect(
            lambda: self.guardar_detalle_venta(servicio_detalle_venta, formulario_detalle_venta,
                                               self.tableLista_detalle_venta)
        )

        self.btn_mostrar_todas_ventas.clicked.connect(
            lambda: self.mostrar_todos_ventas(servicio_venta, self.tableListaVenta)
        )

    '''
    PRODUCTOS
    '''

    def button_handler(self, servicio, widget):
        lista_productos = servicio.hola()
        self.mostrar_lista_productos(widget, lista_productos)

    def mostrar_todos_productos(self, servicio, widget_lista):
        lista_productos = servicio.obtener_todos()
        self.mostrar_lista_productos(widget_lista, lista_productos)

    def mostrar_lista_productos(self, widget, lista_productos):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_productos(widget)

        for index, producto in enumerate(lista_productos):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(producto.id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", producto.nombre))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", producto.marca))
            item = widget.item(index, 3)
            item.setText(_translate("MainWindow", str(producto.precio_unitario)))
            item = widget.item(index, 4)
            item.setText(_translate("MainWindow", str(producto.unidades_stock)))
            item = widget.item(index, 5)
            item.setText(_translate("MainWindow", str(producto.categorias)))
            item = widget.item(index, 6)
            item.setText(_translate("MainWindow", producto.descripcion))
            item = widget.item(index, 7)
            item.setText(_translate("MainWindow", producto.observaciones))

    def limpiar_lista_productos(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_productoDto):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def busqueda_producto_handler(self, servicio, combobox, input_busqueda, widget_lista):
        self.limpiar_lista_productos(widget_lista)
        criterio_busqueda = combobox.currentText()
        texto_busqueda = input_busqueda.text()
        lista_productos = []
        if criterio_busqueda == "Nombre":
            lista_productos = servicio.buscar_por_nombre(texto_busqueda)
        elif criterio_busqueda == "Marca":
            lista_productos = servicio.buscar_por_marca(texto_busqueda)
        elif criterio_busqueda == "Categoria":
            lista_productos = servicio.buscar_por_categoria(texto_busqueda)
        elif criterio_busqueda == "Proveedor":
            lista_productos = servicio.buscar_por_proveedor(texto_busqueda)

        self.mostrar_lista_productos(widget_lista, lista_productos)

    def guardar_producto(self, servicio, formulario_nuevo_producto):
        producto_request = {"nombre": formulario_nuevo_producto["nombre"].text(),
                            "marca": formulario_nuevo_producto["marca"].text(),
                            "categoria": [x.strip() for x in formulario_nuevo_producto["categoria"].text().split(",")],
                            "precio_unitario": formulario_nuevo_producto["precio_unitario"].text(),
                            "unidades_stock": formulario_nuevo_producto["unidades_stock"].text(),
                            "descripcion": formulario_nuevo_producto["descripcion"].text(),
                            "observaciones": formulario_nuevo_producto["observaciones"].text()}
        servicio.guardar(producto_request)

    def cargar_producto_desde_id(self, servicio, input_busqueda, formulario_producto):
        id_producto = input_busqueda.text()
        producto = servicio.buscar_por_id(id_producto)
        formulario_producto["nombre"].setText(producto.nombre)
        formulario_producto["marca"].setText(producto.marca)
        formulario_producto["categoria"].setText(producto.categorias.__str__())
        formulario_producto["precio_unitario"].setText(str(producto.precio_unitario))
        formulario_producto["unidades_stock"].setText(str(producto.unidades_stock))
        formulario_producto["descripcion"].setText(producto.descripcion)
        formulario_producto["observaciones"].setText(producto.observaciones)

    def eliminar_producto(self, servicio, input_busqueda):
        id_producto = input_busqueda.text()
        servicio.eliminar(id_producto)

    '''
    CLIENTES
    '''

    def guardar_cliente(self, servicio, formulario_nuevo_cliente):
        cliente_request = {"nombre": formulario_nuevo_cliente["nombre"].text(),
                           "apellido": formulario_nuevo_cliente["apellido"].text(),
                           "direccion": formulario_nuevo_cliente["direccion"].text(),
                           "localidad": formulario_nuevo_cliente["localidad"].text(),
                           "telefono": formulario_nuevo_cliente["telefono"].text(),
                           "dni": formulario_nuevo_cliente["dni"].text(),
                           "observaciones": formulario_nuevo_cliente["observaciones"].text()}
        servicio.guardar(cliente_request)

    def mostrar_todos_clientes(self, servicio, widget_lista):
        lista_clientes = servicio.obtener_todos()
        self.mostrar_lista_clientes(widget_lista, lista_clientes)

    def limpiar_lista_clientes(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_clienteDto):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def mostrar_lista_clientes(self, widget, lista_clientes):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_clientes(widget)

        for index, cliente in enumerate(lista_clientes):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(cliente.id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", cliente.nombre))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", cliente.apellido))
            item = widget.item(index, 3)
            item.setText(_translate("MainWindow", str(cliente.direccion)))
            item = widget.item(index, 4)
            item.setText(_translate("MainWindow", str(cliente.localidad)))
            item = widget.item(index, 5)
            item.setText(_translate("MainWindow", cliente.telefono))
            item = widget.item(index, 6)
            item.setText(_translate("MainWindow", cliente.dni))
            item = widget.item(index, 7)
            item.setText(_translate("MainWindow", cliente.observaciones))

    def busqueda_cliente_handler(self, servicio, combobox, input_busqueda, widget_lista):
        self.limpiar_lista_clientes(widget_lista)
        criterio_busqueda = combobox.currentText()
        texto_busqueda = input_busqueda.text()
        lista_clientes = []
        if criterio_busqueda == "Nombre":
            lista_clientes = servicio.buscar_por_nombre(texto_busqueda)
        elif criterio_busqueda == "Apellido":
            lista_clientes = servicio.buscar_por_apellido(texto_busqueda)
        elif criterio_busqueda == "Localidad":
            lista_clientes = servicio.buscar_por_localidad(texto_busqueda)
        elif criterio_busqueda == "Provincia":
            lista_clientes = servicio.buscar_por_provincia(texto_busqueda)

        self.mostrar_lista_clientes(widget_lista, lista_clientes)

    def cargar_cliente_desde_id(self, servicio, input_busqueda, formulario_cliente):
        id_cliente = input_busqueda.text()
        cliente = servicio.buscar_por_id(id_cliente)
        formulario_cliente["nombre"].setText(cliente.nombre)
        formulario_cliente["apellido"].setText(cliente.apellido)
        formulario_cliente["direccion"].setText(cliente.direccion)
        formulario_cliente["localidad"].setText(cliente.localidad)
        formulario_cliente["telefono"].setText(cliente.telefono)
        formulario_cliente["dni"].setText(cliente.dni)
        formulario_cliente["observaciones"].setText(cliente.observaciones)

    def actualizar_cliente(self, servicio, formulario_cliente, input_busqueda_id):
        id_cliente = input_busqueda_id.text()
        cliente_request = {"id": id_cliente, "nombre": formulario_cliente["nombre"].text(),
                           "apellido": formulario_cliente["apellido"].text(),
                           "direccion": formulario_cliente["direccion"].text(),
                           "localidad": formulario_cliente["localidad"].text(),
                           "telefono": formulario_cliente["telefono"].text(),
                           "dni": formulario_cliente["dni"].text(),
                           "observaciones": formulario_cliente["observaciones"].text()}
        servicio.actualizar(cliente_request)

    def eliminar_cliente(self, servicio, input_busqueda):
        id_cliente = input_busqueda.text()
        servicio.eliminar(id_cliente)

    '''
    PROVEEDORES
    '''

    def guardar_proveedor(self, servicio, formulario_nuevo_proveedor):
        proveedor_request = {"nombre": formulario_nuevo_proveedor["nombre"].text(),
                             "direccion_comercial": formulario_nuevo_proveedor["direccion_comercial"].text(),
                             "localidad": formulario_nuevo_proveedor["localidad"].text(),
                             "telefono": formulario_nuevo_proveedor["telefono"].text(),
                             "email": formulario_nuevo_proveedor["email"].text(),
                             "dni": formulario_nuevo_proveedor["dni"].text(),
                             "cbu": formulario_nuevo_proveedor["cbu"].text(),
                             "banco_cbu": formulario_nuevo_proveedor["banco_cbu"].text(),
                             "cuit": formulario_nuevo_proveedor["cuit"].text(),
                             "categoria_iva": formulario_nuevo_proveedor["categoria_iva"].text(),
                             "observaciones": formulario_nuevo_proveedor["observaciones"].text()}
        servicio.guardar(proveedor_request)

    def limpiar_lista_proveedores(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_proveedorDto):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def mostrar_lista_proveedores(self, widget, lista_proveedores):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_proveedores(widget)

        for index, proveedor in enumerate(lista_proveedores):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(proveedor.id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", proveedor.nombre))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", proveedor.direccion_comercial))
            item = widget.item(index, 3)
            item.setText(_translate("MainWindow", str(proveedor.localidad)))
            item = widget.item(index, 4)
            item.setText(_translate("MainWindow", str(proveedor.telefono)))
            item = widget.item(index, 5)
            item.setText(_translate("MainWindow", proveedor.email))
            item = widget.item(index, 6)
            item.setText(_translate("MainWindow", str(proveedor.dni)))
            item = widget.item(index, 7)
            item.setText(_translate("MainWindow", str(proveedor.cbu)))
            item = widget.item(index, 8)
            item.setText(_translate("MainWindow", str(proveedor.banco_cbu)))
            item = widget.item(index, 9)
            item.setText(_translate("MainWindow", str(proveedor.cuit)))
            item = widget.item(index, 10)
            item.setText(_translate("MainWindow", str(proveedor.categoria_iva)))
            item = widget.item(index, 11)
            item.setText(_translate("MainWindow", proveedor.observaciones))

    def busqueda_proveedor_handler(self, servicio, combobox, input_busqueda, widget_lista):
        self.limpiar_lista_proveedores(widget_lista)
        criterio_busqueda = combobox.currentText()
        texto_busqueda = input_busqueda.text()
        lista_proveedores = []
        if criterio_busqueda == "Nombre":
            lista_proveedores = servicio.buscar_por_nombre(texto_busqueda)
        elif criterio_busqueda == "Localidad":
            lista_proveedores = servicio.buscar_por_localidad(texto_busqueda)
        elif criterio_busqueda == "Provincia":
            lista_proveedores = servicio.buscar_por_provincia(texto_busqueda)

        self.mostrar_lista_proveedores(widget_lista, lista_proveedores)

    def mostrar_todos_proveedores(self, servicio, widget_lista):
        lista_proveedores = servicio.obtener_todos()
        self.mostrar_lista_proveedores(widget_lista, lista_proveedores)

    def cargar_proveedor_desde_id(self, servicio, input_busqueda, formulario_proveedor):
        id_proveedor = input_busqueda.text()
        proveedor = servicio.buscar_por_id(id_proveedor)
        formulario_proveedor["nombre"].setText(proveedor.nombre)
        formulario_proveedor["direccion_comercial"].setText(proveedor.direccion_comercial)
        formulario_proveedor["localidad"].setText(proveedor.nombre)
        formulario_proveedor["telefono"].setText(proveedor.telefono)
        formulario_proveedor["dni"].setText(proveedor.dni)
        formulario_proveedor["cbu"].setText(proveedor.cbu)
        formulario_proveedor["banco_cbu"].setText(str(proveedor.banco_cbu))
        formulario_proveedor["cuit"].setText(proveedor.cuit)
        formulario_proveedor["categoria_iva"].setText(proveedor.categoria_iva)
        formulario_proveedor["observaciones"].setText(proveedor.observaciones)

    def actualizar_proveedor(self, servicio, formulario_nuevo_proveedor, input_busqueda_id):
        id_proveedor = input_busqueda_id.text()
        proveedor_request = {"id": id_proveedor,
                             "nombre": formulario_nuevo_proveedor["nombre"].text(),
                             "direccion_comercial": formulario_nuevo_proveedor["direccion_comercial"].text(),
                             "localidad": formulario_nuevo_proveedor["localidad"].text(),
                             "telefono": formulario_nuevo_proveedor["telefono"].text(),
                             "email": formulario_nuevo_proveedor["email"].text(),
                             "dni": formulario_nuevo_proveedor["dni"].text(),
                             "cbu": formulario_nuevo_proveedor["cbu"].text(),
                             "banco_cbu": formulario_nuevo_proveedor["banco_cbu"].text(),
                             "cuit": formulario_nuevo_proveedor["cuit"].text(),
                             "categoria_iva": formulario_nuevo_proveedor["categoria_iva"].text(),
                             "observaciones": formulario_nuevo_proveedor["observaciones"].text()}
        servicio.actualizar(proveedor_request)

    def eliminar_proveedor(self, servicio, input_busqueda):
        id_proveedor = input_busqueda.text()
        servicio.eliminar(id_proveedor)

    '''
    CATEGORIAS
    '''

    def guardar_categoria(self, servicio, formulario_nueva_categoria):
        categoria_request = {"nombre": formulario_nueva_categoria["nombre"].text(),
                             "observaciones": formulario_nueva_categoria["observaciones"].text()}
        servicio.guardar(categoria_request)

    def buscar_categoria(self, servicio, input_busqueda, widget_lista):
        self.limpiar_lista_categorias(widget_lista)
        texto_busqueda = input_busqueda.text()
        lista_categorias = servicio.buscar_por_nombre(texto_busqueda)
        self.mostrar_lista_categorias(widget_lista, lista_categorias)

    def mostrar_todas_categorias(self, servicio, widget_lista):
        lista_categorias = servicio.obtener_todas()
        self.mostrar_lista_categorias(widget_lista, lista_categorias)

    def mostrar_lista_categorias(self, widget, lista_categorias):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_categorias(widget)

        for index, categoria in enumerate(lista_categorias):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(categoria.id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", categoria.nombre))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", categoria.observaciones))

    def limpiar_lista_categorias(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_categoriaDto):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def cargar_categoria_desde_id(self, servicio, input_busqueda, formulario_categoria):
        id_categoria = input_busqueda.text()
        categoria = servicio.buscar_por_id(id_categoria)
        formulario_categoria["nombre"].setText(categoria.nombre)
        formulario_categoria["observaciones"].setText(categoria.observaciones)

    def actualizar_categoria(self, servicio, formulario_categoria, input_busqueda_id):
        id_categoria = input_busqueda_id.text()
        categoria_request = {"id": id_categoria, "nombre": formulario_categoria["nombre"].text(),
                             "observaciones": formulario_categoria["observaciones"].text()}
        servicio.actualizar(categoria_request)

    def eliminar_categoria(self, servicio, input_busqueda):
        id_categoria = input_busqueda.text()
        servicio.eliminar(id_categoria)

    '''
    LOCALIDADES
    '''

    def mostrar_todas_localidades(self, servicio, widget_lista):
        lista_localidades = servicio.obtener_todas()
        self.mostrar_lista_localidades(widget_lista, lista_localidades)

    def limpiar_lista_localidades(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_localidadDto):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def mostrar_lista_localidades(self, widget, lista_localidades):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_localidades(widget)

        for index, localidad in enumerate(lista_localidades):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(localidad.localidad_id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", localidad.nombre))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", localidad.codigo_postal))
            item = widget.item(index, 3)
            item.setText(_translate("MainWindow", localidad.provincia))

    def guardar_localidad(self, servicio, formulario):
        localidad_request = {"nombre": formulario["nombre"].text(),
                             "codigo_postal": formulario["codigo_postal"].text(),
                             "provincia": formulario["provincia"].text()}
        servicio.guardar(localidad_request)

    def cargar_localidad_desde_id(self, servicio, input_busqueda, formulario_localidad):
        id_localidad = input_busqueda.text()
        localidad = servicio.buscar_por_id(id_localidad)
        formulario_localidad["nombre"].setText(localidad.nombre)
        formulario_localidad["codigo_postal"].setText(localidad.codigo_postal)
        formulario_localidad["provincia"].setText(localidad.provincia)

    def buscar_localidad(self, servicio, input_busqueda, widget_lista):
        self.limpiar_lista_localidades(widget_lista)
        texto_busqueda = input_busqueda.text()
        lista_localidades = servicio.buscar_por_nombre(texto_busqueda)
        self.mostrar_lista_localidades(widget_lista, lista_localidades)

    def actualizar_localidad(self, servicio, formulario_localidad, input_busqueda_id):
        id_localidad = input_busqueda_id.text()
        localidad_request = {"id": id_localidad,
                             "nombre": formulario_localidad["nombre"].text(),
                             "codigo_postal": formulario_localidad["codigo_postal"].text(),
                             "provincia": formulario_localidad["provincia"].text()}
        servicio.actualizar(localidad_request)

    def eliminar_localidad(self, servicio, input_busqueda):
        id_localidad = input_busqueda.text()
        servicio.eliminar(id_localidad)

    '''
    BANCOS
    '''

    def mostrar_todos_bancos(self, servicio, widget_lista):
        lista_bancos = servicio.obtener_todos()
        self.mostrar_lista_bancos(widget_lista, lista_bancos)

    def limpiar_lista_bancos(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_bancoDto):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def mostrar_lista_bancos(self, widget, lista_bancos):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_bancos(widget)

        for index, banco in enumerate(lista_bancos):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(banco.id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", banco.nombre))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", banco.observaciones))

    def guardar_banco(self, servicio, formulario):
        banco_request = {"nombre": formulario["nombre"].text(),
                         "observaciones": formulario["observaciones"].text()}
        servicio.guardar(banco_request)

    def cargar_banco_desde_id(self, servicio, input_busqueda, formulario_banco):
        id_banco = input_busqueda.text()
        banco = servicio.buscar_por_id(id_banco)
        formulario_banco["nombre"].setText(banco.nombre)
        formulario_banco["observaciones"].setText(banco.observaciones)

    def buscar_banco(self, servicio, input_busqueda, widget_lista):
        self.limpiar_lista_bancos(widget_lista)
        texto_busqueda = input_busqueda.text()
        lista_bancos = servicio.buscar_por_nombre(texto_busqueda)
        self.mostrar_lista_bancos(widget_lista, lista_bancos)

    def actualizar_banco(self, servicio, formulario_banco, input_busqueda_id):
        id_banco = input_busqueda_id.text()
        banco_request = {"id": id_banco,
                         "nombre": formulario_banco["nombre"].text(),
                         "observaciones": formulario_banco["observaciones"].text()}
        servicio.actualizar(banco_request)

    def eliminar_banco(self, servicio, input_busqueda):
        id_banco = input_busqueda.text()
        servicio.eliminar(id_banco)

    '''
    DETALLE VENTAS
    '''

    def agregar_detalle_venta(self, servicio, formulario, widget_lista):
        lista_detalle_ventas = self.obtener_elementos_lista(widget_lista)
        detalle_venta = {"producto": formulario["producto"].text(), "cantidad": formulario["cantidad"].text(),
                         "precio": formulario["precio"].text()}
        lista_detalle_ventas.append(detalle_venta)
        self.mostrar_lista_detalle_venta(widget_lista, lista_detalle_ventas)
        formulario["producto"].setText("")
        formulario["cantidad"].setText("")
        formulario["precio"].setText("")

    def guardar_detalle_venta(self, servicio, formulario, tabla_detalle_ventas):
        lista_detalle_ventas = {}
        lista_detalle_ventas["lista"] = self.obtener_elementos_lista(tabla_detalle_ventas)
        lista_detalle_ventas["cliente"] = formulario["cliente"].text()
        lista_detalle_ventas["forma_pago"] = formulario["forma_pago"].text()
        servicio.guardar(lista_detalle_ventas)
        self.limpiar_lista_detalle_ventas(tabla_detalle_ventas)
        formulario["producto"].setText("")
        formulario["cantidad"].setText("")
        formulario["precio"].setText("")
        formulario["cliente"].setText("")
        formulario["forma_pago"].setText("")

    def mostrar_lista_detalle_venta(self, widget, lista_detalle_venta):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_detalle_ventas(widget)

        for index, detalle_venta in enumerate(lista_detalle_venta):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", detalle_venta["producto"]))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", detalle_venta["cantidad"]))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", detalle_venta["precio"]))

    def obtener_elementos_lista(self, widget_lista):
        lista_detalle_ventas = []
        for index in range(10):
            detalle_venta = {}
            item = widget_lista.item(index, 0)
            detalle_venta["producto"] = item.text()
            item = widget_lista.item(index, 1)
            detalle_venta["cantidad"] = item.text()
            item = widget_lista.item(index, 2)
            detalle_venta["precio"] = item.text()
            if detalle_venta["producto"] != '' and detalle_venta["cantidad"] != '' and detalle_venta["precio"] != '':
                lista_detalle_ventas.append(detalle_venta)

        return lista_detalle_ventas

    def limpiar_lista_detalle_ventas(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_detalle_ventas):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    '''
    VENTAS
    '''

    def mostrar_todos_ventas(self, servicio, widget_tabla):
        lista_ventas = servicio.obtener_todos()
        self.mostrar_lista_ventas(widget_tabla, lista_ventas)

    def mostrar_lista_ventas(self, widget, lista_ventas):
        _translate = QtCore.QCoreApplication.translate
        self.limpiar_lista_ventas(widget)

        for index, venta in enumerate(lista_ventas):
            item = widget.item(index, 0)
            item.setText(_translate("MainWindow", str(venta.id)))
            item = widget.item(index, 1)
            item.setText(_translate("MainWindow", str(venta.fecha)))
            item = widget.item(index, 2)
            item.setText(_translate("MainWindow", venta.forma_pago))
            item = widget.item(index, 3)
            item.setText(_translate("MainWindow", str(venta.total_venta)))
            item = widget.item(index, 4)
            item.setText(_translate("MainWindow", str(venta.cliente)))

    def limpiar_lista_ventas(self, widget):
        _translate = QtCore.QCoreApplication.translate
        for i in range(Ui_MainWindow.cantidad_filas):
            for j in range(Ui_MainWindow.cantidad_elementos_ventas):
                item = widget.item(i, j)
                item.setText(_translate("MainWindow", ""))

    def mostrar_venta_detallada(self, servicio, input_busqueda, widget_lista):
        id_venta = input_busqueda.text()
        lista_venta_detallada = servicio.buscar_por_id(id_venta)