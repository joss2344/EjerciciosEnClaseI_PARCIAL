import os
os.system('cls' if os.name == 'nt' else'clear')

#condicionales en python
a=int(input("Ingrese un numero: "))

if a==0:
    print(f"El numero {a} es ceroe y no se puede clasificar como par o impar") 

elif a%2==0:
    print(f"El numero {a} es par")

else: 
    print(f"El numero {a} es impar")

