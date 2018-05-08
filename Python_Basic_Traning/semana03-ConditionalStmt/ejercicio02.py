"""
EJERCICIO02:
Si se tiene el peso de dos animales: dinosaurio y un elefante, escribir un programa
que permita calcular cuál de los dos tiene el peso mayor en un determinado momento.
Ejemplo:
Ingrese el peso del dinosaurio: 120.50
Ingrese el peso del elefante: 255.50
El elefante pesa más que el dinosaurio

"""

def main():
    pesoDinosaurio = float(input("Peso del Dinosaurio?: "))
    pesoElefante = float(input("Peso del Elefante?: "))
    mensaje = " tiene mayor peso"
    #
    if(pesoDinosaurio>pesoElefante):
        print("Dinosuario" + mensaje)
    else:
        if (pesoDinosaurio == pesoElefante):
            print("Los dos pesan igual")
        else:
            print("Elefante " + mensaje)
    
main()
