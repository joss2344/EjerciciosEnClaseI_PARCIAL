#aqui se colocan los  ejercicios realizados en las clases anteriores

#ejercicios desarrollados en clase
class EjerciciosClase():
    def __init__(self):
        pass

    #limpiar pantalla
    def limpiar(self):
        import os
        os.system('cls' if os.name == 'nt' else'clear')
        

    #hola mundo
    def holamundo(self):
        print("Hola Mundo")
    
    #operaciones aritmeticas
    def operacionesaritmeticas(self):
        #programa que hace operaciones aritmeticas basicas
        a=10
        b=5

        #suma
        suma=a+b
        print(f"La suma de {a}+{b} es: ",suma)

        #resta
        resta=a-b
        print(f"La resta de {a}-{b} es: ",resta)

        #multiplicacion
        multiplicacion=a*b
        print(f"La multiplicacion de {a}*{b} es: ",multiplicacion)

        #division
        division=a/b
        print(f"La division de {a}/{b} es: ",division)

        #operacion con ingreso de valores a variables
        x=int(input("X: "))
        y=int(input("Y: "))

        #potencia
        potencia=x**y
        print(f"La Potencia de {x}^{y} es: ",potencia)

        #operador de residuo
        residuo=x%y
        print(f"El residuo de {x}%{y} es: ",residuo)

        #raiz cuadrada
        raiz=x**(1/2)
        raiz=y**(1/2)
        print(f"La raiz cuadrada de {y} es: ",raiz)
        print(f"La raiz cuadrada de {x} es: ",raiz)
    
    #condifcionales
    def condicionales (self):
        a=int(input("Ingrese un numero: "))

        if a==0:
            print(f"El numero {a} es ceroe y no se puede clasificar como par o impar") 

        elif a%2==0:
            print(f"El numero {a} es par")

        else: 
            print(f"El numero {a} es impar")
        
        
    #ejercicio 1: programa que calcula el precio de un producto con descuento y ISV
    def ejercicio01(self):
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos: "))

        subtotal = precio * cantidad

        if subtotal >= 10000:
            descuento = subtotal * 0.25
            print(f"Ha obtenido un descuento del 25% por su compra [{descuento:.2f}], ¡¡muchas gracias!!")
            isv = (subtotal - descuento) * 0.15
        else:
            descuento = 0
            isv = subtotal * 0.15

        total = subtotal - descuento + isv
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Descuento: {descuento:.2f}")
        print(f"ISV (15%): {isv:.2f}")
        print(f"Su factura a pagar es de: {total:.2f}")


    
   #programa que calcula la edad de una persona
    def ejercicio02(self):
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

    
    #ciclo for
    def cicflofor(self):
        for i in range (1,11):
            print(i)

    # Ejercicio 3: programa que imprime la tabla de multiplicar de un numero ingresado por el usuario
    def ejercicio03(self):
        x=int(input("Ingrese un numero: "))
        for i in range (1,11):
            print(f"{x} * {i} = {x*i}")

    #ciclo while
    def ciclowhile(self):
        i=0

        while i<10:
            i+=1
            print(i)
    
    #ejercicio 4: programa que imprime la tabla de multiplicar de un numero ingresado por el usuario con ciclo while
    def ciclowhile2(self):
        i=0
        x=int(input("Ingrese un numero: "))

        while i<10:
            i+=1
            print(f"{x} * {i} = {x*i}")
    
    #funciones
    def funciones(self):
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

    #ejercicios con operaciones aritmeticas
    def ejercicio06(self):
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

    #funcion descuento
    def funciondescuento(self):

        print("Descuento")
        precio = float(input("Ingrese el precio: "))
        porcentaje = float(input("Ingrese la cantidad de descuento a aplicar (porcentaje): "))

        descuento = precio * porcentaje / 100
        precio_final = precio - descuento

        print(f"El descuento aplicado es: {descuento:.2f}")
        print(f"El precio con descuento es: {precio_final:.2f}")



    #clase 01
    class Animal:
        def __init__(self, nombre):
            self.nombre=nombre
            
        def comer(self):
            print(f"{self.nombre} Esta comiendo")


    class Perro(Animal):
        def ladrar(self):
            print(f"{self.nombre} esta ladrando")


    class Gato(Animal):
        def correr(self):
            print(f"{self.nombre} esta corriendo")

        def maullar(self):
            print("esta maullando")



    #claseOperaciones Aritmeticas
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


#10 ejercicios de tarea
    def ejercicio01(self):
        #programa que escribe hola mundo

        print("Hola mundo")

    def ejercicio02(self):
        n1 = int(input("Ingrese el primer numero: "))
        n2 = int(input("Ingrese el segundo numero: "))
        suma = n1 + n2
        print("La suma de", n1, "y", n2, "es:", suma)

    def ejercicio03(self):
        lado= int(input("Ingrese el lado del rectangulo: "))
        alto= int(input("Ingrese el alto del rectangulo: "))
        area= lado*alto
        print("El area del rectangulo es:", area)

    def ejercicio04(self):
        n = int(input("Ingrese un numero: "))
        if n > 0:
            print("El numero es positivo")
        elif n < 0:
            print("El numero es negativo")
        else:
            print("El numero es cero")

    def ejercicio05(self):
        n = int(input("Ingrese un numero: "))
        if n % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")

    def ejercicio06(self):
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

    def ejercicio07(self):
        for i in range(1, 11):
            print(i)
    
    def ejercicio08(self):
        n = int(input("Ingrese un numero: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

    def ejercicio09(self):
        n = int(input("Ingrese un numero: "))
        suma = 0
        for i in range(1, n + 1):
            suma += i
        print("La suma de los primeros", n, "numeros es:", suma)

    def ejercicio10(self):
        #programa que hace uuna linea de asteriscos con el tamanio del numero ingresado

        n = int(input("Ingrese un numero: "))
        for i in range(n):
            print("*", end="")
        print()





