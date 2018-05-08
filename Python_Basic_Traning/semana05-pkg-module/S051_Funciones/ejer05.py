"""
EJERCICIO 05
Realice una aplicación en python que teniendo como datos de entrada un número entero
positivo (N no mayor a 30), que representa la cantidad de términos que se desea sumar, y
los valores de a, x e y, permita calcular el resultado de la siguiente sumatoria.
# términos 1 2 3 4 5
Recuerde que la aplicación deberá realizar todas las validaciones necesarias

Ejemplos

Ingrese el número de términos (N): 40
Ingrese el número de términos (N): 5
Ingrese el valor de a: 2.5
Ingrese el valor de x: 1.7
Ingrese el valor de y: 5.5
La sumatoria es: 1.3752

Ingrese el número de términos (N): 6
Ingrese el valor de a: 4.73
Ingrese el valor de x: 2.8
Ingrese el valor de y: 1.25
La sumatoria es: -7.876007993

"""

def pedirDato(titulo):
    val = 0
    while True:
        val = float(input(titulo))
        if(val>0 and val<=30):
            break
    return(val)

def calcularSumatoria(nt,a, x, y):
    n=0.0 #numerador
    d=0.0 #denominador
    s=0.0 #suma
    for i in range (1, nt+1):
        #numerador
        if(i%2 == 0):
            n = i*y
        else:
            n = i*x
        
        #denominador
        d = pow(2*a, i-1)
    
        #calcula el termino y la suma
        if(i%2 == 0 ):
            s+= n/d
        else:
            s-=n/d
    
    #sumatoria
    s=3*s
    return(s)

def main():
    n=int(pedirDato("#Terminos?: "))
    a=pedirDato("a?: ")
    x=pedirDato("x?: ")
    y=pedirDato("y?: ")
    #
    suma = calcularSumatoria(n,a,x,y)
    #
    print("La sumatoria es: " + str(suma))

#
main()