
def crearListas():
    # Creacion de listas
    lista1 = []
    lista2 = [0, 4, 6]
    lista3 = ["hola", "peru",".","com"]
    lista4 = ["mouse", [8, 6, 4], ['a']]
    lista5 = list()
    
    #Agregando elementos a la lista
    lista1.insert(0,'Hola')
    lista2.insert(1,2)
    lista3.insert(1,'@')
    lista4.insert(2,[2,0])
    lista5.insert(0,69)
    
    #imprimir
    print(lista1)
    print(lista2)
    print(lista3)
    print(lista4)
    print(lista5)
#
crearListas()