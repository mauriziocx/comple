"""
Ejercicio 7

En matemáticas, una fracción, número fraccionario, (del vocablo latín frāctus, fractĭo -ōnis, roto, o quebrado)
es la expresión de una cantidad dividida entre otra cantidad; es decir que representa un cociente no efectuado de números. 
Por razones históricas también se les llama fracción común, fracción vulgar o fracción decimal. 
Las fracciones comunes se componen de: numerador, denominador y línea divisora entre ambos (barra horizontal u oblicua). 
En una fracción común  a/b el denominador "b" expresa la cantidad de partes iguales que representan la unidad, 
y el numerador "a" indica cuántas de ellas se toman.

Se pide:
Representar una Fraccion y simplificarla a su minima expresion. 

"""

#class Fraccion(object):
class Fraccion:
    #
    def toString(self):
        return str(self.num) + "/" + str(self.den)
    
    #
    def gcd(self,a,b):
        a = abs(a)
        b = abs(b)

        while(b>0):
            t = a % b
            a = b
            b = t

        if(a==0):
            return(b)
        if(b==0): 
            return(a)


    
    #Constructor de la clase Fraccion
    def __init__(self, num=0, den=0):
        if (den==0):
            print("Error: Denominador Cero")
            SystemExit();
        if(num == 0):
            self.num = 0
            self.den = 1
        if(den<0):
            self.num = -num
            self.den = den
        #        
        g = self.gcd(num,den)
        #
        if(g != 1):
            num = num / g
            den = den / g
        #
        self.num = num
        self.den = den        