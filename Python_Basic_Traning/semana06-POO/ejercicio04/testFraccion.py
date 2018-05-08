'''
Ejercicio 8

Escriba un programa en python que permita solicitar
dos puntos (numerador y denominado) y devuelva la fraccion reducida a su minima
expresion

Ejemplo:

Numerador?: 15
Denominador?: 20

Fraccion Original=>15.0/20.0
Fraccion Reducida=> 3.0/4.0

'''

from cfraccion import Fraccion

def pedirDato(t):
    val = float(input(t))
    return val

def main():
    #Formando la Fraccion
    num = pedirDato("Numerador?: ")
    den = pedirDato("Denominador?: ")
    print("Fraccion Original=>" + str(num) + "/" + str(den))
    
    #Creando un objeto Fraccion
    f = Fraccion(num,den) 

    print("Fraccion Reducida=> " + f.toString())

#    
main()
