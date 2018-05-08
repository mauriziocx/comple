"""A class to represent a two-dimensional point"""

class Punto:
    def __init__(self, x=0, y=0):  
        self.x = x 
        self.y = y 
    
    def toString(self):
        strval = "p(" + str(self.x)
        strval = strval + ", " + str(self.y)
        strval = strval + ")"
        return(strval)

#
p1 = Punto(); # X e Y tienen como valor 0
print(p1);
print("p1=> " + p1.toString())

p2 = Punto(8,7) # X e Y tienen valores 8 y 7
print("p2=> " + p2.toString())

    