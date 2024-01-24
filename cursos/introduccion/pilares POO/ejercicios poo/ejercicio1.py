#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self):
        self._nombre=""
        self._nota=0 
    @property
    def nombre(self):
        print(self._nombre)

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def nota(self):
        print(self._nota)
        
    @nota.setter
    def nota(self,nota):
        self._nota=nota
    @property
    def resultado(self):
        if self._nota < 6 :
            print("Reprobado")
        else:
            print("Aprobado")

estudiante=Estudiante()
estudiante.nombre="Kevin"
estudiante.nota=9
estudiante.nombre
estudiante.nota  
estudiante.resultado