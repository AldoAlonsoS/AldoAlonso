import pickle
import shelve

class Estudiante():
    __nombre = ''
    __correoelectronico = ''
    __contraseña = ''

    def __init__(self, name, mail, password):
        self.__nombre = name
        self.__correoelectronico = mail
        self.__contraseña = password

    #def __str__(self):
    #   pass
        #return f'Nombre:{__nombre} Correo: {__correoelectronico}'

    def saveStud(self):
        file = open('registro2.txt', 'wb')
        pickle.Pickler(file, 4).dump(estudiante)
        pickle.Pickler(file, 4).dump(estudiante2)
        pickle.Pickler(file, 4).dump(estudiante3)
        pickle.Pickler(file, 4).dump(estudiante4)
        pickle.Pickler(file, 4).dump(estudiante5)
        #return f'Nombre:{__nombre} Correo: {__correoelectronico}'

    def readStud(self):
        file = open('registro2.txt', 'rb')
        unpickler = pickle.Unpickler(file)
        estudiantes = unpickler.load()
        file.close()
        print(estudiantes)

    def saveStSh(self):
        with shelve.open('registroshelve.db') as shelf:
            for n, c, p in zip(nombres, correos, contras):
                estudiantes = Estudiante(n, c, p)
                shelf[n] = estudiantes

            for r in shelf:
                print(f'{r}: {shelf[r]}')

    def readStSh(self):
        pass

    def updateStu(self):
        pass

nombres = ['Aldo', 'juan', 'carlos', 'martha']
correos = ['aldo@cinvestav.com', 'juan@cinvestav.com', 'carlos@cinvestav.com', 'martha@cinvestav.com']
contras = ['xxxx', 'yyyy', 'zzzz']
#nombres = ['Aldo','Jesus','Carlos', 'Martha']
#correos = ['aldo@cinvestav.com', 'jesus@cinvestav.com', 'carlos@cinvestav.com', 'martha@cinvestav.com']
estudiante = Estudiante('Aldo', 'aldo@cinvestav.com', 'xxxx')
estudiante2 = Estudiante('Juan', 'juan@cinvestav.com', 'xxxx')
estudiante3 = Estudiante('Carlos', 'carlos@cinvestav.com', 'xxxx')
estudiante4 = Estudiante('Martha', 'martha@cinvestav.com', 'xxxx')
estudiante5 = Estudiante('Alida', 'alida@cinvestav.com', 'xxxx')

estudiante.saveStud()
estudiante.readStud()
estudiante2.saveStud()
estudiante2.readStud()
estudiante3.saveStud()
estudiante3.readStud()
estudiante4.saveStud()
estudiante4.readStud()
estudiante5.saveStud()
estudiante5.readStud()
estudiante.saveStSh()


#file = open('registro.txt', 'wb')
#pickle.Pickler(file, 4).dump(estudiante)
#pickle.Pickler(file, 4).dump(estudiante2)
#pickle.Pickler(file, 4).dump(estudiante3)
#pickle.Pickler(file, 4).dump(estudiante4)
#pickle.Pickler(file, 4).dump(estudiante5)





#if __name__ == '__main__':
#    estudiante = Estudiante('Aldo', 'aldo@cinvestav.com', 'xxxxx')

#    estudiante.mostrarNombre()
#    estudiante.mostrarCorreo()



