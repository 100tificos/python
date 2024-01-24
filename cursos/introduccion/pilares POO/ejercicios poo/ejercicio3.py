#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
# Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
# Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno




class Fabrica():
    def __init__(self,llanta,color,precio):
        self.llanta=llanta
        self.color=color
        self.precio=precio
class Carro(Fabrica):
    def datos(self):
        print("no. de llantas: {} color: {} precio: {}".format(self.llanta,self.color,self.precio))
    

class Moto(Fabrica):
    def datos(self):
        print("no. de llantas: {} color: {} precio: {}".format(self.llanta,self.color,self.precio))


carro=Carro(4,"rojo",350000)
moto=Moto(2,"azul",25000)

carro.datos()
moto.datos()