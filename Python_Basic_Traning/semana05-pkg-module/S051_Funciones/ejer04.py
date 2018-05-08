"""
EJERCICIO 04
Escriba un programa que muestre el factorial de numero dado

Ejemplo:
Factorial de un Numero
 Valor de N:? 5
El factorial es => 120


"""
def pedirNumero(titulo):
    val = 0
    while True:
        val = int(input(titulo))
        if(val>=0):
            break
    return(val)

def factorial(num):
    n=num-1
    f=num
    while (n>=1):
        f=f*n
        n = n - 1
    return(f)

def main():
    n=pedirNumero("Factorial de un Numero\n Valor de N:? ")
    f = factorial(n)
    print("El factorial es => " + str(f))
#
main()