def sumador(n):
    suma = 0;
    contador = 0
    while (contador < n):
        contador = contador + 1
        suma = suma + contador
    return(suma)
#
def main():
    n = int(input("Ingrese un numero: "))
    suma = sumador(n)
    print("La suma de los " + str(n) + " numeros es " + str(suma))
#
main()
