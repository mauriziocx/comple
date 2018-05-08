"""
Ejercicio 1

Una pila (stack en inglés) es una lista ordenada o estructura de datos que permite almacenar
y recuperar datos, el modo de acceso a sus elementos es de tipo LIFO (del inglés 
Last In First Out, «último en entrar, primero en salir») . 

Esta estructura se aplica en multitud de supuestos en el área de informática debido a su 
simplicidad y capacidad de dar respuesta a numerosos procesos.

Se pide:
Implementar en python una pila con operaciones de apilar, desapilar y verificar si está vacía. 

"""



class Pila:

    # Crea una pila vacía.
    def __init__(self):
        # La pila vacía se representa con una lista vacía
        self.items=[]

    # Agrega el elemento x a la pila.
    def push(self, x):
        # Apilar es agregar al final de la lista.
        self.items.append(x)
    
    
    # Devuelve el elemento tope y lo elimina de la pila. 
    # Si la pila está vacía lanza una excepción. """
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    
    # Devuelve True si la lista está vacía, False si no.
    def isEmpty(self):
        return self.items == []            