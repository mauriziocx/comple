"""
Ejercicio 05.	

Escriba un programa que solicite el ingreso de un número entre el 1 y el 9 (necesariamente) 
y luego muestre la tabla de multiplicar del número ingresado.

Ejemplo:

Ingrese un numero: 8

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80 

"""

def main():
    num = int(-1)
    resultado=""
    #
    #-------------------------------------
    while(True):
        num=int(input("Ingrese un numero: "))
        if (num>=1 and num<=9):
            break

    #-------------------------------------
    for i in range (1,11):
        resultado = resultado + str(num) + " x " + str(i) + " = " + str(num*i)
        print(resultado)
        resultado=""
    #-------------------------------------        

#
main()
