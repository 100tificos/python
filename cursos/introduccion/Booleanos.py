#variables booleanas
'''verdadero=True
falso=False
print(type(verdadero))'''

#OPERADORES DE COMPARACION
'''num1=1500
num2=1200
num3=1500
cadena1="primera cadena"
cadena2="segunda cadena o ultima"
print(num1>num2) #devuelve True
print(num1<num2)#devuelve False
print(num1>=num3)#devuelve True
print(num1==num2)#devuelve False
print(num1==num3)#devuelve True
print(num1!=num2)#devuelve True
print(num1!=num3)#devuelve False
print(cadena1<cadena2)#devuelve True por el tamaño de la cadena'''

#OPERADORES LOGICOS 
'''print(10>2 and 9>100)#devuelve False
print(10>2 and 23==23)#devuelve True
print(102<=122 or 6>45)#devuelve true
print(not 99!=99)#devuelve True
print(not 100<120)#devuelve False'''


#METODOS BOOLEANOS 
cadena="Ejemplo de cadena"
cadena1="MAYUSCULA"
cadena2="minuscula"
print(cadena.startswith("E"))#Startswith verifica si la variable empieza con el parametro puesto entre parentesis
print(cadena.startswith("a"))
print(cadena.endswith("a"))#endswith verifica si la variable termina con el parametro puesto entre parentesis
print(cadena1.isupper())#verifica si la cadena esta en mayusculas
print(cadena2.islower())#verifica si la cadena esta en minusculas 