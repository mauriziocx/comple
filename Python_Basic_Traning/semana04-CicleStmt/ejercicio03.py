"""
3.	Escriba un programa que calcule e imprima la suma 
    todos los números 
    impares desde cero hasta un número N dado como dato.

Ejemplo: 
Ingrese N?: 10
La suma es 1 + 3 + 5 + 7 + 9 = 25
"""

def main():
    num=int(input("Ingrese N?: "))
    resultado=""
    suma = 0
    #-------------------------------------
    i=1
    while(i<=num):
        resultado = resultado + str(i) + " + "
        suma = suma + i
        i=i+2
        
    #-------------------------------------
    resultado = resultado + " = " + str(suma)
    print(resultado)

#
main()
