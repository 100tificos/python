#IF ELSE
'''edad=19

if edad >= 18:

    print("eres mayor de edad :)")
else:
    print("no eres mayor de edad :(")'''

#ELIF

'''vocal=input("ingrese su vocal: ")'''
'''if vocal.upper()=="A":
    print("su vocal es la A")
elif vocal.upper()=="E":
    print("su vocal es la E")
elif vocal.upper()=="I":
    print("su vocal es la I")
elif vocal.upper()=="O":
    print("su vocal es la O")
elif vocal.upper()=="U":
    print("su vocal es la U")
else:
    print("esa no es una vocal")'''

'''if vocal.upper() in "AEIOU": #in es "en" para saber si esta dentro de 
    print("Es una vocal")
else:
    print("no es vocal")'''

#EJERCICIO
'''numero=int(input("ingrese un numero:"))

if numero>0:
    print("el valor absoluto de {} es {}".format(numero,numero))
else:
    print("el valor absoluto de {} es {}".format(numero,numero*-1))
    print("el valor abosluto de {} es".format(numero),abs(numero))#abs convierte en absoluto un numero
    #print("el valor abosluto de {} es {}".format(numero,abs(numero)))'''

# EJERCICIO2
letra1=input("ingrese su palabra: ")
letra2=input("ingrese su palabra: ")

if letra1[-3:] == letra2[-3:]:
    print("si riman")
elif letra1[-2:] == letra2[-2:]:
    print("riman un poco")
    
else:
    print("no riman")


#operadores ternarios

edad = int(input("Por favor ingrese su edad "))

mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad"
print(mensaje)
