#definir una tupla
mi_tupla = 1, False, 'Edward', 0.145
print(mi_tupla)

#asignar una tupla con una funcion 
def retornar_estudiante():
    return 'Edward', 28, 8.6

tupla_estudiante = retornar_estudiante()
print(tupla_estudiante)

#asignar varios valores desde una tupla como objetos independientes 

nombre_estudiante , edad_estudiante, promedio_estudiante = retornar_estudiante()
print("info estudiante ",nombre_estudiante,edad_estudiante,promedio_estudiante)

#one line suapping
#ejemplo que ek valor de la variable 1 se le asigne el de la variable 2 y el de la variable 2 se le asihne al de la varibale uno

#*****ejemplo poco eficiente*****
variable_1 = 1.0
variable_2 = 2.0

variable_temp = variable_1
variable_1 = variable_2
variable_2 = variable_temp

print(variable_1,variable_2)

#usando suapping
v_1 = 3.1
v_2 = 3.4

v_1, v_2 = (v_2, v_1)

print(v_1, v_2)




