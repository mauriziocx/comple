"""
Nombre: Modulo MyLibCinematica
Proposito: Implementa funciones para encontrar la combinacion y
           permutacion 

"""

def factorial(num):
    res = 1
    x = num
    while(x>0):
        res=res*x
        x-=1
    return(res)

def combinar(n, k):
    nk = n-k
    c = factorial(n) / (1.0 * factorial(k)*factorial(nk))
    return(c)


def permutar(n, k):
    nk = n-k
    c = factorial(n) / (1.0 * factorial(k)*factorial(nk))
    return(c)
