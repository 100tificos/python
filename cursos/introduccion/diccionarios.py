#DICCIONARIOS
'''diccionario={"usuario":"usu","contraseña":1234}

print(diccionario)
print(type(diccionario))
print(diccionario.keys())#muestra solo las llaves
print(diccionario.values())#muestra los valores


print(diccionario["contraseña"])#muestra el valor de una llave en especifico

diccionario["peso"]="30 kg" #agregamos una nueva llave a diccionario
print(diccionario)

diccionario["contraseña"]=4567 #asi modificamos una llave
print(diccionario)'''

#METODOS DICCIONARIOS

'''diccionario={1:2,2:3,3:4}
diccionario2={5:6,6:7,7:8}
diccionario.pop(3)#pop recibe una llave y la elimina
print(diccionario)
#diccionario.clear()  borra todo el diccionario

print(diccionario.get(2))#get devuelve el valor de la llave 

diccionario.setdefault(4,5)#setdefault agrega un nuevo valor (llave,valor)
print(diccionario)

diccionario.update(diccionario2)#actualiza el diccionario agregando los valores del otro diccionario
print(diccionario)

diccionario.copy()#genera una copia del diccionario
print(diccionario)'''

#ejercicio1
'''paises={"Guatemala": "Ciudad de Guatemala", "Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais=input("ingrese el pais: ")
opc=pais.title() in paises #esto arrojara True o False
#if pais.capitalize() in paises:   (esto es otra forma)
if opc==True:
    print(paises[pais.capitalize()])
   
else:
   print("ese pais no se encuentra")'''

#Ejercicio2
jugadores={ 1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

jugador=int(input("ingrese el numero de jugador: "))
if jugador in jugadores:
    print(jugadores[jugador])
   
else:
   print("ese jugador no se encuentra")
