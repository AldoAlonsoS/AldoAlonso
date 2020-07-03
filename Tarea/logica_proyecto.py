from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from ui_proyecto import Ui_MainWindow
from estudiante import Estudiante
import socket as s
import pickle
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.conectar.clicked.connect(self.conexion_servidor)
        self.ui.enviarinfo.clicked.connect(self.registrar)
        self.ui.buscar.clicked.connect(self.buscarArchivo)
        self.ui.ennviararchivo.clicked.connect(self.buscarArchivo)


    @Slot()
    def conexion_servidor(self):
        if self.ui.conectar.text() == 'Conectar':
            try:
                self.cliente = s.socket()
                self.cliente.connect((self.ui.ip.tex(), int(self.ui.puerto.text())))
                self.ui.estado.setText('Conectado')
                self.ui.conectar.setText('Desconectar')
            except:
                e = sys.exc_info()[1]
                self.show_error(str(e))
        elif self.ui.conectar.text() == 'Desconectar':
            self.cliente.close()
            self.ui.setText('Desconectado')
            self.ui.conectar.setText('Conectar')



        #print('Conectado al servidor...')

        #msg = 'Iniciozip'
        #bytes = msg.encode()

        #cliente.send(bytes)

        #while True:

            #data = cliente.recv(500)
            #print(data)

            #if data == b'':
                #print('Finzip')
                #break

        #cliente.close()
        #pass


    @Slot()
    def registrar(self):
        tmp = Estudiante(self.ui.nombre.text(), self.ui.correo.text(), self.ui.contrasenia.text())
        print(f'Persona Registrada {tmp.nombre()}')

        file = open('RegistroProyecto.txt', 'wb')
        pickle.dump(tmp, file)
        file.close()

    @Slot()
    def buscarArchivo(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'Image Files(*.txt)')
        file = open(filename[0], 'rb')

        count = 0
        size = 0

        f2 = open('copiaimg.png', 'wb')

        # for i in file:

        i = file.read(500)
        msg = 'Iniciozip'
        bytes = msg.encode()
        self.cliente.send(bytes)

        while i:
            f2.write(i)

            print(f'[{count + 1}:{len(i)}] {i}')
            count += 1

            size += len(i)
            i = file.read(500)

        msg = 'Finzip'
        bytes = msg.encode()
        self.cliente.send(bytes)

        f2.close()
        file.close()





if __name__=='__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()