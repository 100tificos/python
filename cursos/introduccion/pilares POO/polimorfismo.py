#Polimorfismo es cuando heredas todo de una clase pero modificas algun metodo de esa clase en la clase hijo a pesar de ser heredada
#Polimorfismo:modificacion de clases heredadas y ocupacion de distintos objetos con los mismos metodos
class Animales():
    def __init__(self,mensaje):
        self.mensaje=mensaje

    def Hablar(self):
        print(self.mensaje)

class Perro(Animales):
    
    def Hablar(self):
        print("yo hago guofff!")
        

class Pez(Animales):
    def Hablar(self):
        print("yo hago hablo")

perro=Perro("Miua!")#si heredas siempre sepone el parametro aunque el modificado no lo ocupe
perro.Hablar()

animal=Animales("miau!")
animal.Hablar()

pez=Pez("miau!")
pez.Hablar()