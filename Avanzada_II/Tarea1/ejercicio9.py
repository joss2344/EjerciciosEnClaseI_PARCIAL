#programa que suma los primeros n numeros del 1 al numero ingresdado

n = int(input("Ingrese un numero: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los primeros", n, "numeros es:", suma)
