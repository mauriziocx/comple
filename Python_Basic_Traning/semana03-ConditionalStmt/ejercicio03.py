"""
EJERCICIO03: 
Escribir un programa que permita calcular
las raíces de la ecuación cuadrática y permita
evaluar la ecuación para un valor dado. 

Valida que:
-El discriminante sea mayor a 0.
-La ecuación cuadrática es: Ax2 + Bx + C

Ejemplo
Ingrese el valor de A: 3
Ingrese el valor de B: 6
Ingrese el valor de C: 1
Ingrese un valor para evaluar: 10
Raíz 1: -0.18
Raiz 2: -1.82
3(10)^2 + 6(10) + 1 = 361

"""
from math import pow #para calcular las potencias y raices cuadradas

def raicesEcuacion():
    print("Raices para la ec de la forma: AX^2 + BX + C");
    A = int(input("Valor de A? "))
    B = int(input("Valor de B? "))
    C = int(input("Valor de C? "))
    #
    X = int(input("Ingrese un valor para evaluar: "))
    x1 = x2= 0
    #
    D = pow(B,2)-4*A*C #Calcula el Discriminante
    #
    if (A == 0 ):
        print("La ecuacion no es cuadratica")
    else:
        if(D == 0):
            print("Ec. con raices imaginarias")
        else:
            x1= (-1*B+pow(D,0.5))/(2*A)
            x2= (-1*B-pow(D,0.5))/(2*A)
            print("x1: " + str(x1))
            print("x2: " + str(x2))
            #3(10)^2 + 6(10) + 1 = 361
            res = A*pow(10,2) +B*10 + C
            print(str(A)+"("+str(X)+")^2 + " + 
                  str(B)+"("+str(X)+") + " + 
                  str(C))
            
#
raicesEcuacion()