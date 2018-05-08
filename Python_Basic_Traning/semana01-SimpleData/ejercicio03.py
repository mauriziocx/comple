"""
Ejercicio 18:
Determinar si un numero de tres digitos es CAPICUA

"""
import math

#funcion principal
def main():
    #inicializa la varible numero con un valor de 161
    numero = int(161)
    # inicializa tres variables centena, decena y unidad con valor 0
    centena=int(0)
    decena = int(0)
    unidad = int(0)
    
    centena = math.trunc(numero/100)
    decena = (numero%100)/10
    unidad = (numero%100)%10
    
    if centena == unidad:
        print("El numero es capicua")
    else:
        print("El numero NO es capicua")
    
    dat = "mayor" if (centena>=6) else "menor"
    
    print(dat);

#invocacion a la funcion principal
main()
    
    