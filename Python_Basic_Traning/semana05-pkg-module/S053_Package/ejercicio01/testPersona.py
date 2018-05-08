from pkgperson.person import salario

def calcularSalario():
    print("Calculando Salario")
    sal = salario()
    print("Salario Neto: " + str(sal))
#
calcularSalario()