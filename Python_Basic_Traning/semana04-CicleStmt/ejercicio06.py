"""
Ejercicio 06.	

Escriba un programa que permita determinar la suma de los n primeros 
pares y los m primeros número impares.

Tanto n y m, son número enteros que deberán ser ingresados por el 
usuario y representan la cantidad de números que desean operar.

Ejemplo:

# de pares a sumar?: 4
# de impares a sumar?: 5

Sumatoria de pares=2+4+6+8 = 20

Sumatoria de impares=1+3+5+7+9= 25


"""

def main():
    n=int(input("# de pares a sumar?: "))
    m=int(input("# de impares a sumar?: "))

    sumaPares=0
    sumaImpares=0
    
    resPares=""
    resImpares=""
    #
    #---- calcula suma pares ----------------------------
    i=1
    while(i<=n):
        resPares = resPares + str(2*i) + " + "
        sumaPares = sumaPares + (2*i)
        i=i+1
    
    print("Sumatoria de pares = " + resPares + " = " + str(sumaPares))
    
    
    #
    #---- calcula suma impares ----------------------------
    i=0
    while(i<m):
        resImpares = resImpares + str(2*i + 1) + " + "
        sumaImpares = sumaImpares + (2*i + 1)
        i=i+1
    
    print("Sumatoria de Impares = " + resImpares + " = " + str(sumaImpares))
 

#
main()

