
class Estudiante():
    _nombre = ''
    _correoelectronico = ''
    _contraseña = ''

    def __init__(self, name, mail, password):
        self._nombre = name
        self._correoelectronico = mail
        self._contraseña = password

    def mostrarNombre(self):
        print('Nombre:', self._nombre)
    def mostrarCorreo(self):
        print('Correo: ', self._correoelectronico)

if __name__ == '__main__':
    estudiante = Estudiante('Aldo', 'aldo@cinvestav.com', 'xxxxx')

    estudiante.mostrarNombre()
    estudiante.mostrarCorreo()
