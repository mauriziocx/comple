"""
Ejercicio 5:

En matematica, un vector (también llamado vector euclidiano o vector geométrico) es una magnitud física definida 
en un sistema de referencia que se caracteriza por tener módulo (o longitud) y una dirección (u orientación).

Se pide:
Representar un vector como un punto en el plano cartesiano (2D), las componentes del vector son x e y
que representan los valores de las coordenadas cartesianas.
"""

class Vector(object):

    #Devuelve un nuevo punto, con la resta entre dos puntos.
    def restar(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)

    #Devuelve el modulo del vector
    def modulo(self):
        return (self.x*self.x + self.y*self.y)**0.5

    # Devuelve la distancia entre ambos puntos.
    def distancia(self, otro):
        r = self.restar(otro)
        return r.modulo()


    # Indica si un valor es numérico o no.
    def esNumero(self,valor):
        return isinstance(valor, (int, float, long, complex))

    #Constructor de Punto, x e y deben ser numéricos
    def __init__(self, x=0, y=0):
        #if esNumero(x):
            self.x=x
            self.y=y
        #else:
        #    raise TypeError("x e y deben ser valores numéricos")
#