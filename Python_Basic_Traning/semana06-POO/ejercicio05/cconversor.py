'''
Ejercicio 9 
La temperatura es una magnitud referida a las nociones comunes de calor medible mediante 
un termómetro, el cual puede ser calibrados de acuerdo a una multitud de escalas que dan lugar a 
unidades de medición de la temperatura.

La escala más extendida es la escala Celsius, llamada «centígrada»; y, en mucha menor medida, y 
prácticamente solo en los Estados Unidos, la escala Fahrenheit.

Se pide:

Crear un clase en Python que permita la conversion entre grados centigrados/celsius a farenheit

'''

class Conversor:
    def gradosCentiToFarenheit(self,tempf):
        tempc = (tempf-32)*5.0/9.0
        return(tempc)
    
    def gradosFarengheitToCenti(self,tempc):
        tempf = tempc * 9.0/5.0 + 32
        return(tempf)