import os
os.system('cls' if os.name == 'nt' else'clear')

# Ejercicio 3: programa que imprime la tabla de multiplicar de un numero ingresado por el usuario
x=int(input("Ingrese un numero: "))
for i in range (1,11):
    print(f"{x} * {i} = {x*i}")