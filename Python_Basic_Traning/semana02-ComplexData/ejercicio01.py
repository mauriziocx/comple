
"""
Ejercicio 1
Amigos.SAC es una empresa que está rifando un horno microondas entre sus clientes. 
Cuando un cliente realiza una compra debe registrar sus datos para el sorteo. 
Los datos a registrar son: Numero teléfono y nombre. El gerente conocedor de sus 
habilidades de programación le ha solicitado cargar toda la información en un programa en 
Python para buscar el nombre del ganador. ¿Cómo lo implemen

"""

import random

def main():
    x = []
    total = 0
    n = 10
    
    for i in range (0,n):
        x.append(random.randint(15,95))
        print(x[i])
        total = total + x[i]
    
    promedio = float(total/len(x))
    
    print("suma=>" + str(total))
    print("promedio=> "+ str(promedio))

if __name__ == '__main__':
    main()


