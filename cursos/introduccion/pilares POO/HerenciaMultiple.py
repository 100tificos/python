class A():
    def Primera(self):
        return "esta es la clase A"
class B():
    def Segunda(self):
        return "esta e la clase B"

class C(A,B):#esta clase sera hija tanto de la clase A como de la B
    pass
    
c=C()
print(c.Primera())
print(c.Primera())
