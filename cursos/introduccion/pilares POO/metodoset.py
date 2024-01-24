class A():
    def __init__(self):
        self._cuenta=0
        self._contador=0

    @property 
    def contador(self):
        return self._contador

    @contador.setter#el decorador para el metodo set se agrega el nombre del atributo que modificaremos y la palabra reservada ".setter" para que python reconosca el metodo de tipo set 
    def contador(self,contador):#aunque lleva el mismo nombre que el metodo get python lo distingue como diferente ya que hace diferente funcion y tiene un diferente decorador 
        self._contador=contador


    @property
    def cuenta(self):
        return self._cuenta

    @cuenta.setter
    def cuenta(self,cuenta):
        self._cuenta=cuenta

a=A()
print(a.contador)
a.contador=20
print(a.contador)
print(a.cuenta)
a.cuenta=35
print(a.cuenta)
