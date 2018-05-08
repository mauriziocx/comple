"""
Escriba un programa que permita imprimir los cinco primeros números positivos.
Datos de entrada: Ninguno
Datos de salida: Impresión de los cinco primeros números positivos
Restricciones: Ninguna

"""

def main():
    contador = 1
    while (contador <= 5):
        print("numero => " + str(contador))
        contador = contador + 1
#
main()
