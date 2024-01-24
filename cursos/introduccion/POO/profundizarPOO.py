from tkinter import colorchooser
from numpy import MAY_SHARE_EXACT
from prometheus_client import CollectorRegistry


class FabricaTelefonos():
    def __init__(self,marca,*colores,**modelos):#puede ser self o this pero para buenas practicas se utiliza el self 
        self.marca= marca
        self.colores=colores
        self.modelos=modelos
    
telefono=FabricaTelefonos("nokia","negro","rojo",m1=500,m2=1000)#los atributos los reconoce ya que marca(es un solo elemento),*colores(es una tupla y lleva varios elementos) y **modelos (es un diccionario y lleva diferente sintaxi a la tupla)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria=512 #este es un atributo creado de manera temporal
print(telefono.memoria)