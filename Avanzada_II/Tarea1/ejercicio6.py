#ejercicio quee determina el mayor de 3 numeros

n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
n3= int(input("Ingrese el tercer numero: "))

if n1 > n2 and n1 > n3:
    print("El mayor es:", n1)
elif n2 > n1 and n2 > n3:
    print("El mayor es:", n2)
elif n3 > n1 and n3 > n2:
    print("El mayor es:", n3)
elif n1 == n2 and n1 > n3:
    print("El mayor es:", n1)
elif n2 == n3 and n2 > n1:
    print("El mayor es:", n2)
elif n1 == n3 and n1 > n2:
    print("El mayor es:", n1)
else:
    print("Todos los numeros son iguales")
    