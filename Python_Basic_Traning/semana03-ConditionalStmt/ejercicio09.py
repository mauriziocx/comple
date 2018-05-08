"""
El nivel de avance de un alumno dentro de una universidad se determina, 
según el número de créditos cumplidos hasta la fecha (ver tabla). 

--------------------------------------
Créditos Acumulados     Año académico
--------------------------------------
Menos que 32            Primer año
32 a 63                 Segundo año
64 a 95                 Tercer año
96 o más                Cuarto año
--------------------------------------

Usando esta información, escribir un programa que acepte el número de 
créditos que ha acumulado un estudiante y determine en qué año académico 
se encuentra, mostrando los resultados por pantalla 

Ejemplo: 
Ingrese la cantidad de créditos acumulados: 76 
El alumno se encuentra en el TERCER AÑO

"""

def main():
    
    creditos = int(input("Creditos Acumulados?: "))
    a = str("x")
    
    if (creditos<32):
        a = "Primer año"
    elif(creditos>= 32 and creditos<= 63):
        a = "Segundo año"
    elif (creditos>= 64 and creditos<= 95):
        a = "Tercer año"
    elif (creditos > 96):
        a = "Cuarto año"
    #
    print("Estudiante se encuenta en el " + a.upper())
    
#
main()