from math import pi

class Esfera(object):
	def __init__(self, r=0):
	    self.radio = r
	# método set/get
	def setRadio(self,radio):
	    self.radio = radio
	def getRadio(self):
	    return (self.radio)
	# métodos de servicio, responsabilidades
	def volumen(self):
	    v = 4.0/3.0*pi*(self.radio ** 3)
	    return(v)
#
e = Esfera(10)
print("volumen => {%.2f}" % e.volumen())