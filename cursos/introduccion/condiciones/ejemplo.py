paises={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais=input("ingrese el pais:")

if pais.title() in paises:
    print(paises[pais.title()])

else:
    print("Ese pais no se encuentra en el diccionario")