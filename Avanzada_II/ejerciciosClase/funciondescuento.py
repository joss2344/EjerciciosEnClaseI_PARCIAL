#ejercicios con operaciones aritmeticas

#suma
def suma(x,y):
    return x+y

#resta
def _resta(x,y):
    return x-y

#multiplicacion
def multiplicacion():
    x=int(input("Ingrese un numero: "))
    y=int(input("Ingrese otro numero: "))
    return x*y

#division
def division(x,y):
    return x/y

#exponencial
def exponencial(x,y):
    return x**y

#modulo
def modulo(x,y):
    return x%y

#funcion para descuento
def descuento(precio, porcentaje):
    return precio - (precio * porcentaje / 100)


#llamar las funciones
#suma
print("Suma")
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
print(f"La suma de {x} y {y} es: {suma(x,y)}")
input("Presione enter para continuar...")

#resta
print("Resta")
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
print(f"La resta de {x} y {y} es: {_resta(x,y)}")
input("Presione enter para continuar...")

#multiplcacion
print("Multiplicacion")
print("La multiplicacion es: ",multiplicacion())
input("Presione enter para continuar...")

#division
print("Division")
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
print(f"La division de {x} y {y} es: {division(x,y)}")
input("Presione enter para continuar...")

#exponencial
print("Exponencial")
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
print(f"La exponencial de {x} y {y} es: {exponencial(x,y)}")
input("Presione enter para continuar...")

#modulo
print("Modulo")
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
print(f"El modulo de {x} y {y} es: {modulo(x,y)}")
input("Presione enter para continuar...")

#descuento
print("Descuento")
precio=int(input("Ingrese el precio: "))
descuento=int(input("Ingrese la cantidad de descuento a aplicar: "))
print(f"El precio con descuento es: {descuento(precio,descuento)}")
input("Presione enter para continuar...")

