lista=[20,50,"curso","python",3.14]
print("esta es la lista original: ",lista)
dato1=int(input("dame un dato:"))
dato2=input("dame otro dato:")

lista[0]=dato1
lista[1]=dato2
print("esta es la nueva lista:", lista)
lista[0] *= 2 #si ponemos un operador antes del igual este operador actuara con el numero despues del igual
lista[1] *= 2
print(lista)