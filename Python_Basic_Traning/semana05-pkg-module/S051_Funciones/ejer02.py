"""
EJERCICIO 02
---------------
Escriba un programa en C++ que calcule e imprima el valor de la sumatoria de 
los N primeros términos de la serie.

Suma =  1 -  1/2 + 1/4 - 1/6 + 1/8 -  ... 


Ejemplo: Ingrese N: 3
La suma es: 0.75

"""

def pedirDato(titulo):
    val=0
    while True:
        val=int(input(titulo))
        if(val>=0):
            break
        
    return(val)

def calcularSumatoria(nt):
    numerador = 1.0
    denominador=0.0
    suma=0.0
    
    for i in range(1,nt+1):
        denominador=pow(2,(i-1))
        if(i%2 == 0):
            suma =suma - (numerador/denominador);
            print("- " + str(suma))
        else:
            suma =suma + (numerador/denominador);
            print("+ " + str(suma))
    return(suma)

def main():
    n=pedirDato("Numero de terminos a sumar en la serie?: ")
    resultado = calcularSumatoria(n)
    print("sumatoria es=> " + str(resultado))
    

#
main()