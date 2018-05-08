"""
EJERCICIO01

Escribir un programa en C++ que teniendo como dato de entrada un número entero,
determine si el número es par o impar.
Ejemplo
Ingrese un número entero: 364
Es un número par

"""

def main():
    num = int(input("Ingrese un numero entero: "))
    residuo = num % 2
    #
    if residuo == 0:
        print("El numero es PAR")
    else:
        print("El numero es IMPAR")

main()