#listas

'''lista=['python',414,'nombre',3.14]
print(type(lista))
print(lista[2])
print(len(lista))
lista[3]=5
print(lista)'''

#dedabado
'''lista=[1,2,3,4,"cinco","seis",7,8,"nueve","diez"]
print(lista[5])
print(lista[0:5]) #imprime los elementos del 0 al 5
print(lista[:2]) #desde el inicio hasta el 2
print(lista[6:])#desde el 6 hasta el fin
print(lista[-2])
print(lista[-3:])'''

#metodos listas
'''lista=[5,1,2,3,5,4,5]
lista2=[5,6,4,1,2,3]
print(lista)
lista.append(6)#append agrega un elemento a la lista
print(lista)
lista.append("python")
print(lista)

lista.insert(2, 2.5)#insert inserta un elemento en la lista (posicion,elemento)
print(lista)

print(lista.count(5))#cuenta cuantos elementos repetidos hay en la lista (elemento buscado)
print(lista.index(4))#busca en toda la lista el elemento (elemento buscado) 
print(lista2)
lista2.sort()#ordena una lista en ascendente
print(lista2)
lista2.reverse()#ordena una lista en descendente
print(lista2)

print(lista)
lista.pop()#toma el ultimo dato y lo elimina
print(lista)
lista.remove(2.5)#busca el valor en la lista y lo elimina
print(lista)'''

#llenado de lista
'''lista1=[1,2,3]
lista2=[4,5,6]

lista3=lista1+lista2
print(lista3)'''

'''lista=[]
edad=int(input("ingresa tu edad: "))
lista.append(edad)
print(lista)'''

#ejercicio1
lista=[20,50,"curso","python",3.14]
'''print("esta es la lista original: ",lista)
dato1=input("dame un dato:")
dato2=input("dame otro dato:")

lista[0]=dato1
lista[1]=dato2
print("esta es la nueva lista:", lista)'''

lista[0] *= 2 #si ponemos un operador antes del igual este operador actuara con el numero despues del igual
print(lista)

#extend en lista permite extenderla con otra lista 
lista_numeros = [1,2,3]
lista_extendidas = [4,5,6]

lista_numeros.extend(lista_extendidas)

print(lista_numeros)

#clear limpia totalmente la lista

lista_numeros.clear()

print(lista_numeros)

