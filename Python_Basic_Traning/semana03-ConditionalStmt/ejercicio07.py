"""
La universidad ofrece una beca de 30% para los estudiantes que cumplan ciertos requisitos,
luego de haber culminado el primer ciclo de su carrera. Los requisitos son los siguientes:
 Tener un promedio ponderado mayor o igual a 15.
 No tener ninguna falta.
Con esta información elabore un programa que determine el otorgamiento de una
beca. Los datos que debe ingresar son la nota y la cantidad de faltas.

"""

def main():
    nota = float(input("Ingese Calificacion/Nota?: "))
    faltas = float(input("# de Faltas?: "))
    
    if(nota>=15 and faltas == 0):
        print("Otorgar la Beca al estudiante")
    else:
        print("Estudiante sin posiblidad de beca")
    

main()