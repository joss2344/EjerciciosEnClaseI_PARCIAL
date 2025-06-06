import os
os.system('cls' if os.name == 'nt' else'clear')


#programa que calcula la edad de una persona
edad=int(input("Ingrese el anio de su nacimiento: "))

print("Su edad es: ",2025-edad)
mayor=2025-edad

#verifica si es mayor de edad
if mayor>21:
    print("Usted es mayor de edad")

elif mayor==21:
    print("Usted tiene 21 años y ya eres ciudadano")
else:
    print("Usted es menor de edad")




   
    



