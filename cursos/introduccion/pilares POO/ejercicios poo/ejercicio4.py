from pygame import init


#Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". 
# Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". 
# Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro


class Marino():
    def hablar(self):
        print("Hola...")
class Pulpo(Marino):
    def hablar(self):
        print("soy un pulpo")
        
class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje=mensaje   
        print(self.mensaje)


marino=Marino()
pulpo=Pulpo()
foca=Foca()

marino.hablar()
pulpo.hablar()
foca.hablar("soy pulpo")
