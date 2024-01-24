class A():
    def __init__(self):
        self._cuenta=0
        self._contador=0

    @property #property es un decorador que permite mandar a llamar al metodo sin usar paretesis por ejemplo print(a.contador) /sin property -> print(a.contador())
    def contador(self):#metodo get muestra los atributos privados en pantalla
        return self._contador
    #se recomienda que cad a atributo tenga su metodo get

    @property
    def cuenta(self):
        return self._cuenta

a=A()
print(a.contador)
print(a.cuenta)

