"""
Ejercicio 3
La repartición de ganancias en una empresa se hace en forma proporcional al número de
Acciones de cada uno de sus tres socios. Dada la ganancia de un año y la cantidad de acciones de  cada  
socio,  realice  un  programa en Python que permita:
•	Almacenar/Mostrar en una lista los nombres de cada socio.
•	Almacenar/Mostrar en una tupla los datos de los tres socios (nombre y monto)
•	Determine el monto que le corresponde a cada socio.
•	Mostrar el monto de aportación, dado un socio determinado.

"""

def main():
    print("Datos del Socio 1")
    nombre1 = input('Nombre?: ')
    acciones1  = float(input("Acciones?: "))
    #
    print("Datos del Socio 2")
    nombre2 = str(input('Nombre?: '))
    acciones2 = float(input('Acciones?: '))
    #
    print("Datos del Socio 3")
    nombre3 = str(input('Nombre?: '))
    acciones3 = float(input('Acciones?: '))
    
    print("Operacion Economica Anual")
    ganancia = float(input('Ganancia Anual?: '))
    totalAcciones = acciones1 + acciones2 + acciones3
    
    
    #--------------------------------------------------------------------
    # Determine el monto que le corresponde a cada socio.
    #--------------------------------------------------------------------    
    monto1 = ganancia*(acciones1/totalAcciones)
    monto2 = ganancia*(acciones2/totalAcciones)
    monto3 = ganancia*(acciones3/totalAcciones)
    
    #--------------------------------------------------------------------
    # Almacena/Mostra en una lista los nombres de cada socio.
    #--------------------------------------------------------------------
    listaSocios = list()
    listaSocios.append(nombre1)
    listaSocios.append(nombre2)
    listaSocios.append(nombre3)
    print("\n")
    print(".:: CONTENIDO DE LA LISTA ::.")
    print(listaSocios)

    #--------------------------------------------------------------------
    # AlmacenarMostra en una tupla los datos de los tres socios (nombre y monto)
    #--------------------------------------------------------------------
    t1 = (nombre1, monto1)
    t2 = (nombre2, monto2)
    t3 = (nombre3, monto3)
    tuplaSocios1 = t1 + t2 + t3
    tuplaSocios2 =( t1 , t2 , t3 )
    
    print("\n")
    print(".:: CONTENIDO DE LAS TUPLAS::. ")
    print(tuplaSocios1)
    print(tuplaSocios2)
    #-------------------------------------------------------------------
    # Mostrar el monto de aportacion para un socio determinado
    #-------------------------------------------------------------------
    montosocios = list()
    montosocios.append(monto1)
    montosocios.append(monto2)
    montosocios.append(monto3)
    print(".:: CONTENIDO DE LA LISTA - MONTOS DE CADA SOCIO ::.")
    print(montosocios)
    
    numsocio = int(input("Buscar monto del socio #? "))
    print(montosocios[numsocio-1])
    
#
main()


