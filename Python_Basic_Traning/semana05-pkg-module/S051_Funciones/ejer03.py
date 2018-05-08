"""
Escriba un programa que solicite un número entero N, y que calcule la sumatoria de 
las n primeras fracciones del tipo:

Suma =  1 +  2/1 + 4/3 + 6/5 + 8/7 +  ... 

Ejemplo:
Ingrese N: 3
La suma es: 4.334

"""
def pedirDato(titulo):
	val = 0
	while True:
	    val = int(input(titulo))
	    if(val>=0):
	        break
	return(val)

def calcularSumatoria(n):
    par=0
    impar=0
    suma=1.0
    for i in range(0,n-1):
        par = 2*(i+1)
        impar = 2*i+1
        suma = suma + par/impar
        print("->" + str(suma))
    return(suma)

def main():
    n = pedirDato("Ingrese Cantidad Numeros: ")
    print("suma es" + str(calcularSumatoria(n)))
#
main()