"""
EJERCICIO 05
Escribir un programa, que permita calcular el precio de una entrada al cine,
considerando lo siguiente:
- Si la persona tiene menos de 18 años pagará 7 soles.
- Si la persona tiene de 18 a 50 años pagará 15 soles.
- Si la persona tiene más de 50 años pagará 5 soles.
Ejemplo:
Ingrese la edad de la persona: 18 años
El precio de la entrada es de 15 soles

"""

def main():
    edad = int(input("Edad de la Persona?: "))
    precio = 0
    #proceso
    if (edad<18):
        precio = 7
    else:
        if(edad>= 18 and edad<=50 ):
            precio = 15
        else:
            precio = 5
    
    print("El precio de la entrada es de " + str(precio) + " soles.")

#
main()