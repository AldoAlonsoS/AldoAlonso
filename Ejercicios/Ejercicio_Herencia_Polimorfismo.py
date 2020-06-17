
class Figura():
    _Tnumero_lados = ''
    _Cnumero_lados = ''
    _sin_lado = ''

    def __init__(self, num, num1, num2):
        self._Tnumero_lados = num
        self._Cnumero_lados = num1
        self._sin_lado = num2


    def esTriangulo(self):
        print('Numero de lados:',self._Tnumero_lados, ' Es un triangulo')

    def esCuadradoRectangulo(self):
        print('Numero de lados:', self._Cnumero_lados, ' Es un cuadrado')
    def esCirculo(self):
        print('Sin lados:', self._sin_lado, ' Es un circulo')

if __name__=='__main__':
    figura = Figura(3, 4, 0)

    figura.esCuadradoRectangulo()
    figura.esCirculo()

class Rectangulo(Figura):
    def __init__(self):
        self._Rnumero_lados = 4

    def esCuadradoRectangulo(self):
        print('Numeros de lados:',self._Rnumero_lados, 'Es un rectangulo')


class Triangulo(Figura):
    def __init__(self):
        self._Tnumero_lados = 3



if __name__=='__main__':
    figura = Figura(3, 4, 0)

    #figura.esTriangulo()
    figura.esCuadradoRectangulo()
    figura.esCirculo()

    r = Rectangulo()
    r.esCuadradoRectangulo()

    t = Triangulo()
    t.esTriangulo()


