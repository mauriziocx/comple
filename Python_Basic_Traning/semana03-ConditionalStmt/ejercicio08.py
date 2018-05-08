"""
Escriba un programa donde se ingrese un número entero de 3 cifras únicamente y
luego se debe determinar si el número ingresado es capicúa. 
Un número capicúa se lee
igual de izquierda a derecha que derecha a izquierda.

Ejemplos: 161, 343, 565.
 Si el número que se ingresa es incorrecto, esto significa no tiene 3 cifras, se debe mostrar
un mensaje: “Número incorrecto”
 Si el número que se ingresa es correcto, se debe mostrar un mensaje: “Es número
capicúa” o “No es número capicúa”

"""
from math import trunc

def main():
    num = int(input("Ingrese numero de 3 cifras:"))
    
    if(num>=100 and num<=999):
        centena = trunc(num/100)
        decena = trunc(num%100)/10
        unidad = trunc(num%100)%10
        
        if (centena == unidad):
            print("El numero ES capicua")
        else:
            print("El numero NO ES capicua")
        
    else:
        print("Numero no tiene 3 cifras")    
    
main()