'''while True:#se repite haste que el valor sea correcto
    try:#try se ponen las instrucciones a ejecutar
        a=int(input("ingrese su edad: "))
        print("tu edad es: ",a)
        break # se finaliza el blucle
    except:#except si nose cumplen las instrucciones 
        print("ingresaste un valor erroneo")
    finally:#haya o no haya error se ejecutra al final 
        print("el proceso a culminado")'''

#excepcion multiple
#ejemplo 1
'''while True:
    try:
        num1=int(input("ingresa un numero:"))
        resultado=100/num1
        print("el resultado es: ",resultado)
        break
    except ZeroDivisionError:#manda error si es dividido entre 0
        print("no se puede dividir entre 0")'''

#ejemplo2
'''while True:
    try:
        a=int(input("ingrese su edad: "))
        print("tu edad es: ",a)
        break 
    except ValueError:#si el valor es erroneo
        print("ingresaste un valor erroneo")'''

#ejemplo3
while True:
    try:
        a=int(input("ingrese su edad: "))
        print("tu edad es: ",a)
        break 
    except KeyboardInterrupt:#si se cancela la ejecucion       cancelacion(ctrl + c)
        print("Cancelaste la ejecucuion :(")
        break