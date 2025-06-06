#clase de constructor

class OperacionesAritmeticas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #SUMA
    def suma(self):
        return self.x+self.y
    
    #RESTA
    def resta(self):
        return self.x-self.y
    
    #MULTIPLICACION
    def multiplicacion(self):
        return self.x*self.y
    
    #DIVISION
    def division(self):
        return self.x/self.y
    

x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))

print("La suma es: ",OperacionesAritmeticas(x,y).suma())
   