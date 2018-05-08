''''
Ejercicio 6:

Escriba un programa en python que permita solicitar
dos puntos y devuelva el modulo del vector formado
por ambos puntos


Ejemplo:

Coordenadas Primer Punto
x? 0
y? 0
Coordenadas Segundo Punto
x? 3
y? 4
Distancia 5.0

'''

from cvector import Vector

def pedirDato(t):
    print(t)
    x = float(input("x? "))
    y = float(input("y? "))
    return x,y

def main():
    #Coordenadas del PRIMER punto
    x,y = pedirDato("Coordenadas Primer Punto")
    a = Vector(x,y) #crea el punto/vector A


    #Coordenadas del SEGUNDO punto
    x,y = pedirDato("Coordenadas Segundo Punto")
    b = Vector(x,y) #crea el punto/vector B

    d = a.distancia(b)
    
    print("Distancia {0}".format(d))

#    
main()



