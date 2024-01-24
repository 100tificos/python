class Animales():
    def __init__(self,nombre):
        self.nombre=nombre
class Perro(Animales):
    def __init__(self, nombre,sonido):#tambien se debe de poner el nombre del atriuto heredado
        self.sonido=sonido
        super().__init__(nombre)#la palabra super hereda el metodo init de la clase padre sintaxis= super().__init__(nombre del atributo)###ojo solo se utiliza si hay otro init en la clase hijo

perro=Perro("firulais","Guaff")
print(perro.nombre)
print(perro.sonido)