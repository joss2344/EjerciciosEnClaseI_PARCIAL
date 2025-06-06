#funciones en python

#definimos la funcion
def saludo(nombre):
    print(f"Hola {nombre}")

#definimos la funcion PI
def _PI():
    return 3.1416

#definimos la funcion suma con dos argumentos
def suma(a,b):
    return a+b

#hacemos el llamado a la funcion
saludo("Funes")

#calcular el diametro de un circulo
r=10
diametro=2*_PI()*r
print(f"El diametro del circulo es: {diametro}")

#funcion suma
a=10
b=20
print("Suma:",suma(a,b))






