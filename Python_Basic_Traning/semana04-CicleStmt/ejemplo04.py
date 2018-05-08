"""
Elaborar un programa que muestre los números pares comprendidos entre 10 y 20 inclusive.
Datos de entrada: Ninguno
Datos de salida: Impresión de los pares entre 10 y 20
Restricciones: Ninguna

"""
def main():
    i=0
    print("Los números pares entre 10 y 20 inclusive son: ")
    # for(i=10;i<=20;i=i+2)
    for i in range (10,21,2):
        print(str(i))
#
main()


