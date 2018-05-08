"""

El gerente de Hidrandina, desea contar con un programa 
que le permita calcular el monto a pagar por sus clientes, 
considerando como dato la cantidad de kilowatts consumidos 
al mes y la zona donde vive. La zona puede ser de 
dos tipos: Zona 1 - Comercial o Zona 2 – Residencial. 

•	Si la zona es Comercial se cobra una tarifa fija de 50 soles, 
    luego por los primeros 100 kilowatts se les cobra 0.75 soles 
    y por cada kilowatt por encima de los 100 se le cobra 0.9 soles. 
•	Si la zona es Residencial, se cobra una tarifa fija de 25 soles, 
    luego por los primeros 100 kilowatts se les cobra 0.30 soles y 
    por cada kilowatt por encima de los 100 se les cobra 0.7 soles. 

Escriba un programa en el que, dados como datos: el consumo y la zona, 
calcule e imprima el monto a pagar. 

Ejemplo: Ingrese zona (1 – 2): 2 
Ingrese consumo: 245
El monto a pagar es: 156.5 soles



"""
def main():
    zona = int(input("Ingrese zona (1 – 2): "))  #2 
    consumo = float(input("Ingrese consumo: ")) #245
    monto=0.0
    tarifaFija = 0.0
    #
    if(zona == 1): #zona comercial
        tarifaFija = 50
        if(consumo>100):
            monto = tarifaFija + 100*0.75 + (consumo-100)*0.90
        else:
            monto = tarifaFija + 100*0.75
    elif (zona == 2 ):
        tarifaFija = 25
        if(consumo>100):
            monto = tarifaFija + 100*0.30 + (consumo-100)*0.70
        else:
            monto = tarifaFija + 100*0.30 
    #
    print("El monto a pagar es: " + str(monto) + " soles")

#main
main()