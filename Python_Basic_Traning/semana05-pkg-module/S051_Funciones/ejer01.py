"""
EJERCICIO 01:

Escriba un programa que muestre que numero que se encuentra en una posicion dada de la serie fibonacci.

Por ejemplo, a continuacion se los primeros 8 numeros de la serie fibonacci. En la posicion 6 se
encuentra el numero 8 de la serie, en la posicion 8 se encuentra en el numero 21
POSICION  : 1  2  3  4  5  6   7   8
SERIE FIBO: 1  1  2  3  5  8  13  21

Restricciones:
* Utilice una funcion para pedir datos
* Utilice una funcion para calcular el numero fibonacci
* Utilice un procedimiento para presentar los resultados


"""

def fibonacci(n):  #es una funcion, retonar un valor
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


def pedirNumero(titulo): # Es una funcion retorna un valor
    x = 0
    while True:
        x = int(input(titulo))
        if(x>0):
            break
    return(x)

def mostrarResultados(n,f): # Es un procedimiento, no retorna valor
    print("El termino " + str (n) + " de la serie fibonacci es " + str(f))


def main():
    n = pedirNumero("# termino fibonacci?=> ")
    f = fibonacci(n)
    mostrarResultados(n,f)
    
main()