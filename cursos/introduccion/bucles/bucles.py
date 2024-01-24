#WHILE
'''i=0
while i<10:
    i += 1
    print("se repite, salto:{}".format(i))'''

#EJERCICIO 1
'''numero=int(input("Dame el numero de la tabla de multiplicar: "))
i=0
while i<10:
    i+=1
    resultado=numero*i
    print("{} * {} = {}".format(numero,i,resultado))'''

#EJERCICIO2
'''edad=int(input("Dame tu edad: "))
i=1
while i != edad:
    print("tu has cumplido:{}".format(i))
    i+=1'''

#FOR
'''lista=["uno","dos","tres"]
tupla=(1,2,3,4,5)
for i in lista:
    print(i)
for j in tupla:
    print(j)'''

#FOR with RANGE
'''for i in range(1 , 10 , 2):#range es el rango(inicio,fin,cada cuantos se mostrara)
    print(i)'''

#BREAK&CONTINUE
'''for i in range(1,10):
    print(i)
    if i == 5:
        break#break para la instruccion aunque aun no se cumpla la condicion''' 

'''for i in range(1,10):
    
    if i == 6:
        continue #continua despues de que la condicion del if sea cumplida (omite)
    print(i)'''

#EJERCICIO1
'''for i in range(1,11):
    print(i)
r1=int(input("Dame rango 1: "))
r2=int(input("Dame rango 2: "))
for i in range(r1,r2+1):
    print(i) '''

#EJERCICIO2
r1=int(input("Dame rango 1: "))
r2=int(input("Dame rango 2: "))
for i in range(r1,r2+1):
    if i % 2 == 0:
        continue
    print(i)