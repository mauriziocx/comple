from mylibcinematica import *


def calculoPosicion():
    vi = float(input("velocidad inicial?: "))
    a = float(input("Aceleracion?: "))
    t = float(input("Tiempo?: "))
    
    d = distancia_ViA(vi,a,t)
    
    print("Distancia=> " + str(d))
#
calculoPosicion()
    
    
    