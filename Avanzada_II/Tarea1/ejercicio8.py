# programa que pide un numero y muestra su tabla de multiplicar

n = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
    