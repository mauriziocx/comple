
def crearListas():
    # Creacion de listas
    lista1 = []
    lista2 = [10, 11, 12]
    lista3 = ["hola@", "peru"]
    lista4 = ["pares", [8, 6, 4]]
    lista5 = list()
    
    #Agregando elementos a la lista
    lista1.extend(['a','e','o'])
    lista2.extend([13,14])
    lista3.extend([".","com"])
    lista4.extend(2,[2,0])
    lista5.extend(0,69)
    
    #imprimir
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)
    print(lista5)
#
crearListas()