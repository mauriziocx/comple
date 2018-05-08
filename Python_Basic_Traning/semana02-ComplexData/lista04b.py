
def crearListas():
    # Creacion de listas
    lista1 = []
    lista2 = [10, 11, 12]
    lista3 = ["hola","@","peru",".","com"]
    lista4 = ["pares", [8, 6, 4]]
    lista5 = list(['a','e','o'])
    
    #Eliminando elementos en la lista
    #lista1.pop() #Error lista vacia

    print(lista2.pop())
    print(lista2)
    
    print(lista3.pop())
    print(lista3)
    
    print(lista4.pop())
    print(lista4)
    
    print(lista5.pop())
    print(lista5)
#
crearListas()