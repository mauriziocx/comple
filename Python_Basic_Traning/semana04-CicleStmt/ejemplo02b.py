"""
Dado un numero n=7 generar 7,6,5,4,3,2,1 .
Datos de entrada: n
Datos de salida: Impresión de la serie de números positivos
Restricciones: Ninguna

"""
def main():
    n=int(input("Cantidad de terminos: "))
    while(n>0):
        print(str(n) + " ")
        n = n - 1
#
main()

