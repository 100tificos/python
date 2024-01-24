class Animales():
    def habla(self):
        print("Hola yo soy un animal")
    def Descripcion(self):
        print("yo soy un {}".format(self.animal))

class Perro(Animales):#al poner una clase dentro de los parametros de otra heredamos de la clase dentro de los parametros los atributo y metodos 
    pass #esta palabra le dice a python que no podremos nada dentro de la clase 

class Abeja(Animales):
    def __init__(self,animal):
        self.animal=animal

animal=Animales()
animal.habla()

perro=Perro()
perro.habla()

abeja=Abeja("abeja")
abeja.Descripcion()