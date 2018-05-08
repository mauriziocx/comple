'''
Ejercicio 10
Escriba un programa que permita convertir grados celcius a centigrados y viceversa

Ejemplo

Grado Centigrados?: 100
Grados Farenheit=> 37.77777777777778

Grados Farenheit?: 37.78
Grados Centigrados=> 100.00399999999999


'''
from cconversor import Conversor

def test():
    c = Conversor()
    
    gc = float(input("Grado Centigrados?: "))
    gf = c.gradosCentiToFarenheit(gc)
    print("Grados Farenheit=> " + str(gf))
    
    print("")
    
    gf = float(input("Grados Farenheit?: "))
    print("Grados Centigrados=> " + str (c.gradosFarengheitToCenti(gf)))

#
test()


