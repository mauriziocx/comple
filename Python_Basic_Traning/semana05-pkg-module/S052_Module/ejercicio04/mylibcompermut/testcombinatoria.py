from libcombinatoria import *

def main():
    n = int(input("Valor de N?: "));
    f = factorial(n)
    print("factorial de " + str(n) + " es " + str(f))
    #
    k = int(input("Valor de K?: "));
    c = combinar(n, k);
    print("combinatoria de " + str(n) + " tomandos de " + str(k)  + " es " + str(c))
    #
    
#
main()
