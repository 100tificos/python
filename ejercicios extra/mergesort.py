#mergesort

#creamos clase
def mergesort(lista):
    #si la lista es mayor a 1 elemento
    if len(lista) > 1 :
        #se asigna el valor de la mitad
        mitad = len(lista) // 2
        #asignamos la primera y segunda mitad
        firstmit = lista[:mitad]
        secondmit = lista[mitad:]

        mergesort(firstmit)
        mergesort(secondmit)
        #definimos 3 variables 
        i=0
        j=0
        k=0
        #se hace el intercambio entre numeros si uno es mayor que otro hasta que el ciclo termine 
        while i < len(firstmit) and j< len(secondmit):
            if firstmit[i] < secondmit[j]:
                lista[k] = firstmit[i]
                i += 1
            else:
                lista[k] = secondmit[j]
                j += 1
            k += 1
        #se actualiza la lista
        while i < len(firstmit):
                lista[k] = firstmit[i]
                i += 1
                k += 1
        while j <len(secondmit):
            lista[k] = secondmit[j]
            j +=1
            k +=1



numeros = [13, 5, 2, 19, 11, 7, 1, 3]
print(numeros)


mergesort(numeros)
print(numeros)
            