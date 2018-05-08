class Animal(object):
    def __init__(self):
        print "Animal creado"

class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)

class Perro(Animal):
    def __init__(self):
        super(Perro, self).__init__()

Gato() 
Perro()