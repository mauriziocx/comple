"""
Nombre: Modulo MyLibCinematica
Proposito: Implementa funciones para encontrar la posicion o distancia
           de una particula, conocida, la velocidad inicial vi, 
           la acelaracion a, el tiempo t, la velocidad final vf.

"""

def distancia_ViA(vi, a, t):
    d = vi*t * 1/2.0*a*pow(t,2)
    return(d)

def distancia_ViVf(vi,vf,t):
    d = (vi+vf)/2.0*t
    return(d)
    

def distancia_ViAn(vi,a,n):
    d = vi + a/2.0*(2*n-1)
    return(d)