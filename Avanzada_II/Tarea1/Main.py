from Ejercicios import *
ejerc= EjerciciosClase()


while True:
            print("================================= MENÚ DE OPCIONES ========================================||")
            print("------------Ejercicios en clase-----------------------------|||------Ejercicio en casa-----||")
            print("1. Ejercicio 1: Hola Mundo                                  |||-15. Ejercicio 1            ||")
            print("2. Ejercicio 2: Operaciones Aritméticas                     |||-16. Ejercicio 2            ||")
            print("3. Ejercicio 3: Condicionales (Par o Impar)                 |||-17. Ejercicio 3            ||")        
            print("4. Ejercicio 4: Total de Compra con ISV y Descuento         |||-18. Ejercicio 4            ||")
            print("5. Ejercicio 5: Cálculo de Edad y Clasificación             |||-19. Ejercicio 5            ||")
            print("6. Ejercicio 6: Ciclo For (1 al 10)                         |||-20. Ejercicio 6            ||")       
            print("7. Ejercicio 7: Tabla de Multiplicar (For)                  |||-21. Ejercicio 7            ||")  
            print("8. Ejercicio 8: Ciclo While (1 al 10)                       |||-22. Ejercicio 8            ||")
            print("9. Ejercicio 9: Tabla de Multiplicar (While)                |||-23. Ejercicio 9            ||")
            print("10.Ejercicio 10: Funciones (Saludo, PI, Suma, Diámetro)     |||-24. Ejercicio 10           ||")      
            print("11.Ejercicio 11: Operaciones Aritméticas con Funciones      |||----------------------------||")
            print("12.Ejercicio 12: Función Descuento                          |||----------------------------||")
            print("13.Ejercicio 13: Clases y Herencia (Animal, Perro, Gato)    |||----------------------------||")
            print("14.Ejercicio 14: Clase Operaciones Aritméticas (POO)        |||----------------------------||")
            print("0. Salir                                                    |||----------------------------||")                      
            print("===========================================================================================||")

            op = input("Seleccione una opción: ")

            match op:
                case "1":
                    ejerc.limpiar()
                    ejerc.holamundo()
                    input("Presione Enter para continuar...")

                case "2":
                    ejerc.limpiar()
                    ejerc.operacionesaritmeticas()
                    input("Presione Enter para continuar...")
                    
                case "3":
                    ejerc.limpiar()
                    ejerc.condicionales()
                    input("Presione Enter para continuar...")

                case "4":
                    ejerc.limpiar()
                    ejerc.ejercicio01()
                    input("Presione Enter para continuar...")

                case "5":
                    ejerc.limpiar()
                    ejerc.ejercicio02()
                    input("Presione Enter para continuar...")

                case "6":
                    ejerc.limpiar()
                    ejerc.cicflofor()
                    input("Presione Enter para continuar...")

                case "7":
                    ejerc.limpiar()
                    ejerc.ejercicio03()
                    input("Presione Enter para continuar...")

                case "8":
                    ejerc.limpiar()
                    ejerc.ciclowhile()
                    input("Presione Enter para continuar...")

                case "9":
                    ejerc.limpiar()
                    ejerc.ciclowhile2()
                    input("Presione Enter para continuar...")

                case "10":
                    ejerc.limpiar()
                    ejerc.funciones()
                    input("Presione Enter para continuar...")

                case "11":
                    ejerc.limpiar()
                    ejerc.ejercicio06()
                    input("Presione Enter para continuar...")
                    
                case "12":
                    ejerc.limpiar()
                    ejerc.funciondescuento()
                    input("Presione Enter para continuar...")

                case "13":
                    ejerc.limpiar()
                    perr=input("Ingrese el nombre del perro: ")
                    ga=input("Ingrese el nombre del gato: ")
                    perro = ejerc.Perro(perr)
                    perro.comer()
                    perro.ladrar()
                    gato = ejerc.Gato(ga)
                    gato.comer()
                    gato.correr()
                    gato.maullar()
                    input("Presione Enter para continuar...")

                case "14":
                    ejerc.limpiar()
                    x = int(input("Ingrese un número: "))
                    y = int(input("Ingrese otro número: "))
                    operaciones = ejerc.OperacionesAritmeticas(x, y)
                    print(f"Suma: {operaciones.suma()}")
                    print(f"Resta: {operaciones.resta()}")
                    print(f"Multiplicación: {operaciones.multiplicacion()}")
                    print(f"División: {operaciones.division()}")
                    input("Presione Enter para continuar...")

                
                case "15":
                    ejerc.limpiar()
                    ejerc.ejercicio01()
                    input("Presione Enter para continuar...")
                
                case "16":
                    ejerc.limpiar()
                    ejerc.ejercicio02()
                    input("Presione Enter para continuar...")

                case "17":
                    ejerc.limpiar()
                    ejerc.ejercicio03()
                    input("Presione Enter para continuar...")

                case "18":
                    ejerc.limpiar()
                    ejerc.ejercicio04()
                    input("Presione Enter para continuar...")

                case "19":
                    ejerc.limpiar()
                    ejerc.ejercicio05()
                    input("Presione Enter para continuar...")

                case "20":
                    ejerc.limpiar()
                    ejerc.ejercicio06()
                    input("Presione Enter para continuar...")
                
                case "21":
                    ejerc.limpiar()
                    ejerc.ejercicio07()
                    input("Presione Enter para continuar...")

                case "22":
                    ejerc.limpiar()
                    ejerc.ejercicio08()
                    input("Presione Enter para continuar...")
                
                case "23":
                    ejerc.limpiar()
                    ejerc.ejercicio09()
                    input("Presione Enter para continuar...")

                case "24":
                    ejerc.limpiar()
                    ejerc.ejercicio10()
                    input("Presione Enter para continuar...")

                case "0":
                    print("Saliendo del programa...")
                    break

                case _:
                    print("Opción no válida. Intente de nuevo.")
