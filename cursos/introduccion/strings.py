'''cadena="esto es una cadena de texto"
cadena2='esto es una "cadena" de texto'
cadena3="esto es una \"cadena\" de texto"
cadena4='esto es una \'cadena\' de texto'
print(cadena)
print(cadena2)
print(cadena3)
print(cadena4)'''

#\n es tabulacion
#\t tabulacion 
#\b quita el espacio entre una palabra y otra 



#STRINGS ARITMETICAS **********************************

'''cadena1="hola Kevin"
cadena2="Marin"
numero=1
print(cadena1 + cadena2)
print(cadena2 * 5)
print(numero,"hola usuario: ",cadena2) #concatenacion 
print(type(str(numero))) #convertir entero a string '''


#DEBADADO DE CADENA 
'''cadena1="esto es un String(debanado de cadena)"

print(len(cadena1)) #len devuelve el tamaño de una cadena 
print(cadena1[5]) #muestra el caracter de la cadena en el que se encuentre el numero dentro del corchete 
print(cadena1[0:10]) #inicio:fin 
print(cadena1[:10]) #si dejamos el valor vacio tomara el inicio o el fin de la cadena 
print(cadena1[5:]) 
print(cadena1[-2]) #si ponemos valores negativos comenzara desde el ultimo
print(cadena1[-10:]) '''

#METODOS DE CADENA 

'''cadena1="Ejemplo Para Metodos"
cadena2="ejemplo2 para metodos"
print(cadena1.lower()) #lower pasa todas las MAys en mins
print(cadena1.upper()) #upper pasa todo de mins a Mays
print(cadena2.capitalize()) #convierte la primera letra en Mays
print(cadena1.title()) #convertira a Mays la primera letra de cada palabra en la cadena 
print(cadena1.swapcase()) #convertira las Mays a mins y las mins a Mays '''

#Remover prefijos y consultas de strings
producto1 = '001 - Manzana'
producto2 = 'Manzana - 001'

print(producto1.removeprefix('001 - '))
print(producto2.removesuffix(' - 001'))

#EJERCICIO 1
'''cadena1="Te quiero solo como amigo"
print(cadena1[0:2])#primeros dos
print(cadena1[-3:])#ultimos 3
print(cadena1[0::2])#imprimir de dos en dos 
print(cadena1[::-1])#alreves
print(cadena1,cadena1[::-1])#bien y alreves'''

#EJERCICIO 2  S,e,p,a,r,a,d,o
'''cadena="eparado"
c=cadena.replace("",",",2)#metodo replace ("caracter reemplazado","sustituto","cuantos reemplazara")
d=cadena.replace("",",")
print("S"+d)'''


