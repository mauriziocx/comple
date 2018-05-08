#from libmath import potencia

from mylibmath import potencia

def seriePotencias(base, numTerminos):
    for i in range (1,numTerminos+1):
        p = potencia(base, i )
        print(str(base) + " " +str(i) + " " + str(p))
#
seriePotencias(2,5)