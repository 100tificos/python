class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()
#esto es hacer una mala practica ya que para ello existe el set y el get
# print(a.cuenta)
# a.cuenta = 20
# print(a.cuenta)

#si el tributo tiene solo un guion bajo quiere decir que es privado como buena practica aunque python permita modificrlo o mostrarlo,si tiene 2 guiones bajos es estrictamente 
# privado y python no dejara modificarlo, aunque solo es necesario con un guion bajo para señalar que es privado 