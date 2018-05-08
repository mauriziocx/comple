"""
Escribir un programa que reciba como datos de entrada los goles del equipo local
(gl) y los goles del equipo visitante (gv), imprima una cadena de caracteres indicando qué
equipo ha ganado (resultados posibles: “local”, “visitante”, “empate”).
Ejemplo:
Ingrese la cantidad de goles del equipo local: 7
Ingrese la cantidad de goles del equipo visitante: 4
Ganó el equipo local

"""

def main():
    gLocal = int(input("Goles equipo Local? "))
    gVisitante = int(input("Goles equipo Visitante? "))
    
    if(gLocal == gVisitante):
        print(" Empate: No hay ganador ")
    else:
        if(gLocal > gVisitante):
            print("Gano el equipo Local ")
        else:
            print("Gano el equipo Visitante")
    
main()