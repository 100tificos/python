#Funciones propias de python 
'''num="70"
print(type(num))#type es una funcion propia de python al igual que int y float o inclusive metodos para la lista etc.
print(type(int(num)))
lista=[12,70,1,-2]
print(len(lista))
print(max(lista))
print(min(lista))'''

#Funciones creadas 
'''def saludo():#def es para crear funciones : palabra reservada def <nombre de la funcion>():<sintaxis>
 print("hola usuario")
saludo()

def tabla7():
    for i in range(11):
        print("7 x {} = {}".format(i,i*7))

tabla7()'''

#Ejercicio1
'''
def addi(li):
    for i in range(10):
        num=int(input("Dame el numero {}: ".format(i)))
        li.append(num)
        i +=1
    print(li)
lista=[]


def parimpar():
    lista.sort()
    par=[]
    impar=[]
    for i in lista:#recorremos la lista con i(i es el indice de cada casilla)
        if i%2==0:
            par.append(i)
        else:
            impar.append(i)
    print(par)
    print(impar)
addi(lista)
parimpar()
'''
#ejercicio2
num=0
def fact():
    num=int(input("Dame un numero entero: "))
    result=1
    for i in range(1,num+1):
        result=result*i
    print(result)
fact()
#tambien puede usarse la libreria math con la funcion "factorial"