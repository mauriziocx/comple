""" 
Ejercicio 4

Utilice una cola para almacenar los primeros diez numeros impares, posteriormente
muestre y quite un elemento de la cola.

"""

from ccola import Cola

def fillCola(p):
    for i in range(1,11):
        p.add(2*i)
    
    for i in range(1,11):
        if (not p.isEmpty()):
            print("Inicio: {0}".format(p.remove()))
#
def main():
    p1=Cola()
    fillCola(p1)
    print(p1.isEmpty()) #pregunta por si la cola esta vacia
#
main()