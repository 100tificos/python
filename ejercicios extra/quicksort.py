#creamos la funcion inicial
def quick_sort(lista):
    #mandamos a llamar a una funcion recusriva con los parametros de lista, inicio y fin
    quick_sort_auxiliar(lista, 0, len(lista) - 1)
#creamos la funcion recursiva 
def quick_sort_auxiliar(lista, inicio, fin):
    #si el inico es menor al fin llamamos a otra funcion recursiva para partir la lista
    if inicio < fin:
        punto_particion = particionar(lista, inicio, fin)

        quick_sort_auxiliar(lista, inicio, punto_particion - 1)
        quick_sort_auxiliar(lista, punto_particion + 1, fin)
#creamos la funcion recursiva
def particionar(lista, inicio, fin):
    #creamos un pivote en la posicion inicio
    pivote = lista[inicio]
#creamos dos variables con el inicio y el fin de la lista como drecha e izquierda
    izquierda = inicio + 1
    derecha = fin
    terminado = False
#un ciclo que acaba cuando terminado es igual a True
    while not terminado:
        #si izquierda es menor a derecha recorremos  1 espacio hacia delante a izquierda 
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1
        #si derecha es mayor a izquierda recorremos  1 espacio hacia atras a derecha
        
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha -= 1
        #si derecha es menor a izquierda terinado cambia a true 
        if derecha < izquierda:
            terminado = True
        else:
            #en caso de que los numeros sean iguales 
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    
    lista[inicio], lista[derecha] = lista[derecha], lista[inicio]

    return derecha


numeros = [9, 4, 3, 22, 7, 10, 15, 1]
print(numeros)
#llamamos al quick sort
quick_sort(numeros)
print(numeros)