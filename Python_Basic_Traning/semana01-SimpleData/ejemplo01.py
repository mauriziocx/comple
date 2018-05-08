
def calcularAreaCirculo():
    radio = float(0.0)  #declara la variable radio de tipo float con valor 0
    PI = float(3.14159) #declara la variable PI con valor3.14159

    print("Radio Circulo? ") #imprime la cadena "Radio Circulo" en la pantalla
    radio = input() #lee el valor del radio desde el teclado y lo almacena en radio
    
    area = PI * radio * radio #calcula el valor del area y lo almacena en una variable llamada area
    
    #str(area) convierte a cadena el valor de area 
    
    print("Area Circulo=> " +str(area)) #imprime la cadena "Area Circulo" concatenada con el 
                                        #valor del area convertido a cadena por str(area)
#
calcularAreaCirculo() #invoca a la funcion calcularAreaCirculo()