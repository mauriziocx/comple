"""
Mostrar la tabla de caracteres ASCII a partir del Código 32 (el espacio en blanco) 
hasta el Código 164 (o sea la ñ) sin incluir las minúsculas (rango del 97 al 122).
Datos de entrada: Ninguno
Datos de salida: Impresión de algunos caracteres ASCII
Restricciones: Ninguna

"""
def main():
    print("Los Caracteres ASCII son: ")
    #for(int i=32;i<=164;i++):
    for i in range(32, 165, 1):
        if(i<97 or i>122):
            print(str(i) + " -> " + chr(i))
#
main()
