""" 
Ejercicio 3

Una cola (también llamada fila) es una estructura de datos, caracterizada por ser una secuencia de elementos en 
la que la operación de inserción push se realiza por un extremo y la operación de extracción pop por el otro. 
También se le llama estructura FIFO (del inglés First In First Out), debido a que el primer elemento en entrar 
será también el primero en salir.

Las colas se utilizan en sistemas informáticos, transportes y operaciones de investigación (entre otros), 
dónde los objetos, personas o eventos son tomados como datos que se almacenan y se guardan mediante colas 
para su posterior procesamiento

Se pide:

Representar a una cola, con operaciones de encolar y desencolar.

"""
class Cola:
    # Crea una cola vacía
    def __init__(self):
        # La cola vacía se representa por una lista vacía
        self.items=[]
    
    # Agrega el elemento x como último de la cola.
    def add(self, x):
        self.items.append(x)
    

    # Elimina el primer elemento de la cola y devuelve su
    # valor. Si la cola está vacía, levanta ValueError.
    def remove(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    # Devuelve True si la cola esta vacía, False si no.
    def isEmpty(self):
        return self.items == []
