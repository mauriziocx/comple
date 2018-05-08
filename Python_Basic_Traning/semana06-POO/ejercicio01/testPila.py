"""
Ejercicio 2

Utilice una pila para almacenar una lista de los primeros 10 numeros
impartes, luego quite y muestre el numero que se encuentra en el tope
de la pila

"""


from cpila import Pila

def fillPila(p):
    for i in range(1,11):
        p.push(2*i+1)
    
    for i in range(1,11):
        if (not p.isEmpty()):
            print("Tope: {0}".format(p.pop()))
#
def main():
    p1=Pila()
    fillPila(p1)
    print(p1.isEmpty()) #pregunta por si la pila esta vacia
#
main()