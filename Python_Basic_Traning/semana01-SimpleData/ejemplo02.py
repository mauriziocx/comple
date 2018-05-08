

def calcularVolumenCubo():
    #declara variables
    lado = float(0)
    volumen = float(0)
    
    #entrada de datos
    lado = input("Longitud del lado del cubo? ")
    
    #proceso
    volumen = lado * lado * lado
    
    #salida
    print("Volumen: " + str(volumen))
    
    
calcularVolumenCubo()
