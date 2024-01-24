#Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
# Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.



class Universidad():
    def universidad(self,nombreuni):
        self.nombreuni=nombreuni

class Carrera():
    def carrera(self,especialidad):
        self.especialidad=especialidad

class Estudiante(Universidad,Carrera):
    def estudiante(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        print("universidad: {} especialidad: {} nombre: {} edad: {}".format(self.nombreuni,self.especialidad,self.nombre,self.edad))

       
        

persona=Estudiante()
persona.universidad("Upiicsa")
persona.carrera("Informatica")
persona.estudiante("Kevin",22)
