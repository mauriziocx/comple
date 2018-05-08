
from math import pi

class Circulo:
   radio = 0

   def __init__(self, radio):
      self.radio = radio

   def area(self):
       a = pi * self.radio * self.radio
       return(a)

   def perimetro(self):
       a = 2*pi * self.radio
       return(a)
#

c=Circulo(10)

print("Area y Perimetro SIN Redondeo")
print("Area=> " + str(c.area()))
print("Perimetro=> " + str(c.perimetro()))

#imprime area y perimetro con dos decimales

print("\nArea y Perimetro CON Redondeo a 3 decimales")

print("area=> {0:.3f}".format(c.area())) #forma 1
print("perimetro=> %.3f" % c.perimetro()) #forma 2 
