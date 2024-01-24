#creacion clase
'''class FabricaTelfonos(): #class <nombre de la clase>()
    pass
#creacion objeto
celular=FabricaTelfonos()'''

#Metodos y atributos 
'''class FabricaTelefno():#se recomienda empezar el nombre con mayuscula
    marca = "Huawei"
    color = "negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self,mensaje):
        return mensaje
    def musica(self):
        print("escuchar musica")


telefono=FabricaTelefno()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar("hola amigo"))
print(telefono.marca)
print(telefono.color)
print(telefono.memoriaRam)
print(telefono.almacenamiento)
telefono.musica()'''

#init y self
'''class FabricaTelefonos():
    marca="samsung"

    def ElaborarHuawei(self):#self sirve para hacer global un atributo,si no tiene self solo toma los atributos de la clase y no de los metodos 
        self.marca="huawei"

telefono=FabricaTelefonos()
print(telefono.marca)
telefono.ElaborarHuawei()
print(telefono.marca)'''

'''class FabricaTelefonos():
    def __init__(self): #init es un metodo de control el cual se ejecutara con el simple hecho de crear el objeto
        print("se esta ejecutando el metodo init")

telefono=FabricaTelefonos()'''

'''class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca=marca #se piden desde los argumentos 
        self.color=color

telefono=FabricaTelefonos("huawei","negro")
print(telefono.marca)
print(telefono.color)'''

#metodos especiales

class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca=marca  
        self.color=color
        print("el objeto {} ha sido creado".format(self.marca))
    def __str__(self):#str rehace la descripcion del objeto cuando este se manda a imprimir
        return "el objeto es {}".format(self.marca)    

    def __del__(self): #del es un metodo destructor que se ejecuta despues de haberse ejecutado el objeto y posteriormente elimina el objeto de la memoria de ejecucion 
        print("el objeto {} ha sido destruido".format(self.marca))

telefono=FabricaTelefonos("huawei","negro") #se ponen los valores dentro del parametro de la clase ya que no podemos mandar a llamar al metodo init ya que este se ejecuta solo
print(telefono.marca)
print(telefono)