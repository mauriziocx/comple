
def crearListas():
    # Creacion de listas
    lista1 = []
    lista2 = [10, 11, 12]
    lista3 = ["hola","@","peru",".","com"]
    lista4 = ["pares", [8, 6, 4]]
    lista5 = list(lista3)
    
    #Buscando elementos en la lista
    #lista1.remove(0) #Error lista vacia
    print(lista1)
    
    lista2.remove(10)
    print(lista2)
    
    lista3.remove("peru")
    print(lista3)
    
    lista4.remove([8,6,4])
    print(lista4)
    
    lista5.remove(".")
    print(lista5)
#
crearListas()