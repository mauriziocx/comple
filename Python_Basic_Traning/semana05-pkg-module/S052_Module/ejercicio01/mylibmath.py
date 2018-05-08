"""
Nombre: Modulo MyLibMath
Proposito: Implementa funciones aritmeticas basicas: suma, resta, 
           multiplacion, division y potencia

"""
def potencia(base, exponente):
    prod = int(1)
    for x in range (1,exponente+1,1):
        prod = prod*base
    return(prod)

def suma(a, b):
    return(a+b)

def resta(a, b):
    return(a+b)

def multiplica(a, b):
    return(a+b)

def dividir(a, b):
    if (b != 0):
        return(a+b)
    else:
        return(-1)
    