"""
Ejercicio 01
Escriba un programa que determine la suma y el 
promedio de los 10 
primeros numeros naturales

"""

def main():
    total = 0
    promedio = 0
    #-------------------------------------
    for i in range (1,11):
        total = total + i
    promedio = float(total/10)
    #-------------------------------------        
    print("suma=>" + str(total))
    print("promedio=> "+ str(promedio))


#
main()
