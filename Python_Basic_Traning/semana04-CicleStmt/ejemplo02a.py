"""
Dado un numero n=7 generar 7,6,5,4,3,2,1 .
Datos de entrada: n
Datos de salida: Impresión de la serie de números positivos
Restricciones: Ninguna

"""

def main():
    n = int(input("Cantidad de terminos?: "))
    cont=1
    serie=n
    while(cont <= n):
        print(str(serie) + " ")
        serie = serie - 1
        cont = cont + 1
#
main()
