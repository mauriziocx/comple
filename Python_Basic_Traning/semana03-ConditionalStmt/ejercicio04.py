"""
EJERCICIO 04:

Escribir un programa que permita calcular el número de pulsaciones
que debe tener una persona por cada 10 segundos de ejercicio aeróbico.

Si la persona es del sexo femenino, la fórmula es:
Número de pulsaciones = (220 – edad) /10 y

Si el sexo es masculino:
Número de pulsaciones = (210 – edad) /10.

Ejemplo:
Ingrese el sexo de la persona (F o M): F
Ingrese la edad de la persona: 24

El número debe ser de 20 pulsaciones por cada 10 segundos aproximadamente

"""
def main():
    #entrada de datos
    sexo = str(input("Sexo(M,F)?: "))
    edad = int(input("Edad?: "))
    #proceso
    np = int(0) #np es Numero de Pulsaciones
    
    if (sexo == 'M'):
        np = (210-edad)/10
    else:
        if (sexo == 'F'):
            np = (220 - edad)/10
        else:
            np=-1
    
    if(np != -1 ):
        print("# pulsaciones debe ser de " + 
        str(round(np)) + " por cada 10 segundo aprox.")
    else:
        print("No se puede determinar")
    
    #salida de datos

main()