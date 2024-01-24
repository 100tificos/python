'''def entero():
    print("entero: ")
    return 10
def flotante():
    print("decimal: ")
    return 5.7
def frase():
    return 'hola'
print(entero())
print(flotante())
print(frase())

def asignacion():
    return 1 ,2 ,3 ,4 ,5

a,b,c,d,e=asignacion()
print(a,b,c,d,e)'''

#Ejercicio1
'''val1=int(input("dame un valor: "))
val2=int(input("dame un valor: "))

def compa():
    if val1>val2:
        return 1
    elif val1<val2:
        return -1
    else:
        return 0
print(compa())'''

#Ejercicio2
'''costo=float(input("Dame el costo: "))
iva=int(input("Dame el porcentaje de iva: "))
result=0
def factu():
    if iva < 1:
        result=(0.21*costo)+costo
        return result
    else:
        result=((iva/100)*costo)+costo
        return result
print(factu())'''

#Parametros y argumentos 
'''def suma(num1,num2):#cuando se ponen parametros dentro de la funcion se puede reutilizar
    res=num1+num2
    return res 


print(suma(10,35))
print(suma(100,40))'''

#variables globales
'''def valores():
    global num1 #con la palabra reservada global puedes hace una variable de tipo global(pueden utilizarse dentro y fuera de una funcion)
    global num2
    num1=100
    num2=40
    resul=num1+num2
    return resul

print(valores())

resta=num1-num2
print(resta)'''
#argumentos indefinidos 
'''def argumento(*num):#si se coloca un * antes del nombre de la variable lo tomara como una tupla
    return type(num)
print(argumento(10,2,3,4))'''

#ejercicio1 
'''def cuadrado(base,altura):
    area=base*altura 
    return area

def circulo(radio):
    area=3.14*(pow(radio,2))
    return area

print(cuadrado(2,3))
print(circulo(3))'''
#ejercicio2
def media(lista):
    total=0
    for i in lista:
        total=total+i
    medias=total/2
    return medias
li=[1,2,3,4,5,6,7,8,9,10]
print(media(li))