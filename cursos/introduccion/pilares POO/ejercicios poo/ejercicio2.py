#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
# Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
# Llamar a la clase Calculadora.


class Calculadora():
    def __init__(self):
        self._v1=int(input("Dame un numero: "))
        self._v2=int(input("Dame otro numero: "))
        self._result=0
    
    def Suma(self):
        _result=self._v1+self._v2
        print("{} + {} = {}".format(self._v1,self._v2,_result))
    def Resta(self):
        _result=self._v1-self._v2
        print("{} - {} = {}".format(self._v1,self._v2,_result))
    def Multiplicacion(self):
        _result=self._v1*self._v2
        print("{} * {} = {}".format(self._v1,self._v2,_result))
    def Division(self):
        try:
          _result=self._v1/self._v2
          print("{} / {} = {}".format(self._v1,self._v2,_result))
        except:
            print("no se puede dividir entre cero :'(")


calc=Calculadora()

calc.Suma()
calc.Resta()
calc.Multiplicacion()
calc.Division()
