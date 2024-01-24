##Creamos el objeto
def torrehanoi( n , origen, destino, auxiliar):
    ##condicion si n==1 disco entonces solo hace un movimiento 
    if n == 1:
      print(f'mueve el disco 1 de {origen} a {destino}')
      
      return
      ##si no mueve el disco uno del origen al destino y despues mueve el segundo al auxiliar y regresa el disco uno al destino
    else:
      torrehanoi( n-1, origen, auxiliar, destino)
      print(f'mueve el disco {n} de {origen} a {destino}')
      torrehanoi( n-1, auxiliar, destino, origen)
      

##numero de discos
n = 3
##llamamos el objeto
torrehanoi(n, 'A', 'B', 'C')
