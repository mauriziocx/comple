"""
Ejercicio 4
Una empresa de ventas de motores automóviles necesita un programa en Python que le permita:
•	Almacenar en un SET pares de valores (MarcaAutomovil, ModeloAutomovil)
•	Almacenar en una TUPLE pares de valores (ModeloMotor, NumeroCilindros)
•	Almacenar en una LISTA las marcas de los automóviles
•	Almacenar en un Diccionario (MarcaAutomovil, ModeloAutomovil, NumeroCilindros)
•	Mostrar el contenido del SET, TUPLE y LISTA
•	Mostrar la información de una marca de automóvil en particular.

"""
def main():
    print("Datos de la Primera Marca")
    marca1 = str(input("Marca del auto?: "))
    modelo1 = str(input("Modelo de la marca " + marca1 +" :? "))
    motor1  = str(input("Modelo del motor de la marca " + modelo1 +" :? "))
    cilindro1 = int(input("Numero de cilindros del " + motor1 +" :? "))
    #
    print("Datos de la Segunda Marca")
    marca2 = str(input("Marca del auto?: "))
    modelo2 = str(input("Modelo de la marca " + marca2 +" :? "))
    motor2  = str(input("Modelo del motor de la marca " + modelo2 +" :? "))
    cilindro2 = int(input("Numero de cilindros del " + motor2 +" :? "))
    #
    print("Datos de la tercera Marca")
    marca3 = str(input("Marca del auto?: "))
    modelo3 = str(input("Modelo de la marca " + marca3 +" :? "))
    motor3  = str(input("Modelo del motor de la marca " + modelo3 +" :? "))
    cilindro3 = int(input("Numero de cilindros del " + motor3 +" :? "))
    
    #-----------------------------------------------------------------------
    #Almacenar en un SET pares de valores (MarcaAutomovil, ModeloAutomovil)
    #-----------------------------------------------------------------------
    print("Contenido del SET")
    setAutos = set()
    setAutos.add((marca1, modelo1));
    setAutos.add((marca2, modelo2));
    setAutos.add((marca3, modelo3));
    print(setAutos)
    #
    #-----------------------------------------------------------------------
    #	Almacenar en una TUPLE pares de valores (ModeloMotor, NumeroCilindros)
    #-----------------------------------------------------------------------    
    print("Contenido de la TUPLA")
    t1 = (motor1, cilindro1)
    t2 = (motor2, cilindro2)
    t3 = (motor3, cilindro3)
    tupla1 = (t1, t2, t3)
    print(tupla1)
    
    #-----------------------------------------------------------------------
    # Almacenar en una LISTA las marcas de los automóviles
    #-----------------------------------------------------------------------    
    print("Contenido de la LISTA")
    listMarcas = list()
    listMarcas.append(marca1)
    listMarcas.append(marca2)
    listMarcas.append(marca3)
    print(listMarcas)    

#
main()


