# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(298, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ip = QLineEdit(self.centralwidget)
        self.ip.setObjectName(u"ip")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ip)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.puerto = QLineEdit(self.centralwidget)
        self.puerto.setObjectName(u"puerto")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.puerto)

        self.conectar = QPushButton(self.centralwidget)
        self.conectar.setObjectName(u"conectar")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.conectar)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.nombre = QLineEdit(self.centralwidget)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nombre)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.correo = QLineEdit(self.centralwidget)
        self.correo.setObjectName(u"correo")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.correo)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.contrasenia = QLineEdit(self.centralwidget)
        self.contrasenia.setObjectName(u"contrasenia")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.contrasenia)

        self.enviarinfo = QPushButton(self.centralwidget)
        self.enviarinfo.setObjectName(u"enviarinfo")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.enviarinfo)

        self.buscar = QPushButton(self.centralwidget)
        self.buscar.setObjectName(u"buscar")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.buscar)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_6)

        self.ennviararchivo = QPushButton(self.centralwidget)
        self.ennviararchivo.setObjectName(u"ennviararchivo")

        self.formLayout.setWidget(8, QFormLayout.SpanningRole, self.ennviararchivo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 298, 21))
        self.menuCliente_Aldo_Alonso = QMenu(self.menubar)
        self.menuCliente_Aldo_Alonso.setObjectName(u"menuCliente_Aldo_Alonso")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCliente_Aldo_Alonso.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PUERTO:", None))
        self.conectar.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NOMBRE:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CORREO:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A:", None))
        self.enviarinfo.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
        self.buscar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.ennviararchivo.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
        self.menuCliente_Aldo_Alonso.setTitle(QCoreApplication.translate("MainWindow", u"Cliente<Aldo Alonso>", None))
    # retranslateUi

