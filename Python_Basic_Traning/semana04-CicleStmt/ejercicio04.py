"""
Ejercicio 04

Escriba un programa que imprima todos los múltiplos de 3, 
mayores que cero, que sean menores que un número 
N (positivo) que será ingresado como dato.

Ejemplo: 
Ingrese N: 25
Los múltiplos son: 3 6 9 12 15 18 21 24


"""

def main():
    num=int(input("Ingrese N?: "))
    resultado=""

    #-------------------------------------
    i=0;
    multiplo=1
    
    while(multiplo<=num):
        i=i+1
        resultado = resultado + str(multiplo) + " "
        multiplo = 3*i
    #-------------------------------------
    print("Los multiplos son: " + resultado)

#
main()