class Forma(object):
	def nombre(self, forma):
		print("Forma : %s" %forma)

class Cuadrado(Forma):
	def area(self,lado):
		return(lado**2)

#
def main():
    f = Forma()
    f.nombre("Sin forma");
    g=Cuadrado();
    g.nombre("cuadrado");
    print(str(g.area(10)));

#
main()
    