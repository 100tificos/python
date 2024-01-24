#Declaracion 

mi_set = {1,2,3,4}
print(mi_set)
#agregar datos en un set vacio
otro_set = set()
otro_set.add(1)
otro_set.add(2)
otro_set.add(3)
otro_set.add(4)
#los set no permiten elementos repetidos
otro_set.add(4)
print(otro_set)
#otro ejemplo
lista=[1,2,2,3,4,5,5,6,7,8,8,9]

lista_set = set(lista)
print("lista sin repetidos",lista_set)

#las listas en la busqueda buscan 1 por uno en los elementos y tardan mas ya que la busqueda crece exponencialmente
pertenece = 7 in lista
print(pertenece)

#los sets no porque almacenan la busqueda asi que ellos no buscan uno por uno porque registran que almacenaron dicho resultado
pertenece = 8 in lista_set
print(pertenece)

#cuando python crea un set crea un has table (un elemento hasheable significa que python asignara un numero unico)

frutas = {'manzana',
          'pera',
          'banana'}
'''a cada elemento lo almacena en un espacio con un id unico en memoria 
   usando el hash y aplicandole un % 8 para ver en que casilla esta del 
   hashtable(python siempre crea una de 8 verificando que no supere el 
   66% y si lo supera crece exponencialmente 8,16,32,etc) por ejemplo a
   manzana le asigno 1254785125 que al hacer % 8 nos da 0 entonces nos 
   lo guarda en el upset 0 en caso de que por ejemplo pera lo asigne a 
   upset 0 se recorre al siguiente upset de la table que este vacio por 
   eso cuando colisiona y hace busqueda ya no seria como O(1) si no seria 
   O(n) ya que recorrera hasta que encuentre el valor '''
