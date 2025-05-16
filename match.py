#Explicacion y uso de match

# def suma():
#     n1=int(input("Ingrese un numero:"))
#     n2=int(input("Ingrese otro numero: "))
#     print("El resultado de la suma es: ",n1+n2)
#     suma()
# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("El resultado de la resta es: ",n1-n2)
#     resta()
# def multiplicacion():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("El resultado de la multiplicacion es: ",n1*n2)
#     multiplicacion()
# def division():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("El resultado de la division es: ",n1/n2)
#     division()
#     try:
#         n1=int(input("Ingrese un numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print("El resultado de la division es: ",n1/n2)
#     except ZeroDivisionError as nombre_de_excepcion:
#         print(f"Se produjo una excepcion: {nombre_de_excepcion}")


# def calcu():
#     while True:
#      op=int(input('''Ingrese una opcion: 
#                 1.- Suma
#                 2.- Resta
#                 3.- Multiplicacion
#                 4.- Division
#                 5.- Salir
#                 '''))

#      match op:
#         case 1:
#             print("Suma")
#             suma()
#         case 2:
#             print("Resta")  
#             resta() 
#         case 3:
#             print("Multiplicacion")
#             multiplicacion()
#         case 4:
#             print("Division")
#             division()
#         case 5:
#             print("Saliendo...")
#             break
#         case _:
#             print("Opcion invalida")
# calcu()


# #Nuevo menu recursivo. debe tener 3 programas creados anteriormente el menu debe llamar a estos programas y ejecutarlos de manera correcta debe tener la opcion de salir y la opcion por defecto

# def promedio():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     n3=int(input("Ingrese otro numero: "))
#     print("El promedio es: ",(n1+n2+n3)/3)
#     promedio()
# def factorial():
#     n=int(input("Ingrese un numero: "))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print("El factorial es: ",fact)
#     factorial()
# def potencia():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print("La potencia es: ",n1**n2)
#     potencia()

# def menu():
#     while True:
#      op=int(input('''Ingrese una opcion: 
#                 1.- Promedio
#                 2.- Factorial
#                 3.- Potencia
#                 4.- Salir
#                 '''))

#      match op:
#         case 1:
#             print("Promedio")
#             promedio()
#         case 2:
#             print("Factorial")  
#             factorial() 
#         case 3:
#             print("Potencia")
#             potencia()
#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("Opcion invalida")
# menu()

# def numazar():
#     import random
#     numAzar=random.randint(1,30)

#     print(numAzar)
#     if numAzar>=20:
#         print("Puede pasar")
#     else:
#         print("Le falta puntaje")

#     import random


#     numaadivinar=random.randint(1,50)

#     num=int(input("Adivine el numero:"))

#     while numaadivinar!=num:
#         print(numaadivinar)
#         if num>numaadivinar:
#             print("El numero a adivinar es menor")
#         else:
#             print("El numero a adivinar es mayor")
#         num=int(input("Adivine el numero:"))
#     print("Felicitaciones, adivinaste el numero")
# numazar()

# def votos():
#     (input("Ingrese la cantidad de votantes "))
# Kaiser=int(0)
# lol=int(0)
# votos=int(0)
# print("Por que postulante votara?")
# print("Los postulantes son: Kaiser y lol")

# (input("Por quien quiere votar"))

# if Kaiser > lol:
#     print("Punto para Kaiser")
# else:
#     print("Punto para lol")

# palabra=input("ingrese una pabalabra ")
# caract=0
# for i in palabra:
#     print(i)
#     caract=caract+1
#     caract+1
#     print("la cant de caracteres es", caract)
# num=0
# while num<=(5):
#     print(num)
#     num==5

# resp=("no")

# while resp!=("si"):
#     resp=input("Desea salir del sistema?  :")
# votos()

# def rulrusa():
#     import random

#     barril=random.randint(1,6)
#     rul=int(input("Disparo :"))

#     while barril!=rul:
#         print("Disparo fallido")
#         rul=int(input("Disparo :"))
# print("Disparo exitoso")
# print("Fin del juego")
# rulrusa()

# while True:
#     try:
#         num=int(input("Ingrese un numero mayor que 3: "))
#         if num>3:
#             print("El numero es mayor que 3")
#             break
#         else:
#             print("El numero no es mayor que 3")
#     except ValueError:
#         print("Error, no es un numero")

#Crear in menu de carrito con las siguientes opciones:
# 1.- ingresar nombre del usuario
#sera mostrado en la boleta, con un saludo
# 2.- comprar, poner productos para poder comprar con su precio correspondiente
# 3.- sacar boleta, calcular el precio neto y el precio mas iva. mostrar totales
# 4.- salir
#consideraciones:
#por lo menos 3 productos
#no hay limite de compra
#se puede salir en cualquier momento
#los montos de los productos son fijos
#mostrar  el total de articulos comprados
#definir un precio fijo para cada producto

# def menu():
#     while True:
#         print("Bienvenido al carrito de compras")
#         print("Por favor, elija una opcion:")
#         print("1.- Ingresar nombre del usuario")
#         print("2.- Comprar productos")
#         print("3.- Sacar boleta")
#         print("4.- Salir")
#         opcion = input("Ingrese una opcion: ")
#         match opcion:
#             case "1":
#                 nombre = input("Ingrese su nombre: ")
#                 print(f"Hola {nombre}, bienvenido al carrito de compras") 
#             case "2":
#                 print("Productos disponibles:")
#                 print("1.- Producto 1 - $3000")
#                 print("2.- Producto 2 - $2400")
#                 print("3.- Producto 3 - $1250")
#                 print("4.- Producto 4 - $5000")
#                 print("5.- Producto 5 - $1500")
#                 print("6.- Producto 6 - $2000")
#                 carrito = []
#                 while True:
#                     producto = input("Ingrese el numero del producto que desea comprar (o 'salir' para terminar): ")
#                     if producto == "salir":
#                         break
#                     elif producto in ["1", "2", "3", "4", "5", "6"]:
#                         carrito.append(producto)
#                         print(f"Agregado {producto} al carrito")
#                     else:
#                         print("Producto no valido")
#             case "3":
#                 if not carrito:
#                     print("El carrito esta vacio")
#                 else:
#                     total = 0
#                     for item in carrito:
#                         if item == "1":
#                             total += 3000
#                         elif item == "2":
#                             total += 2400
#                         elif item == "3":
#                             total += 1250
#                         elif item == "4":
#                             total += 5000
#                         elif item == "5":
#                             total += 1500
#                         elif item == "6":
#                             total += 2000
#                     iva = total * 0.21
#                     total_con_iva = total + iva
#                     print(f"Total de articulos comprados: {len(carrito)}")
#                     print(f"Total sin IVA: ${total}")
#                     print(f"IVA: ${iva}")
#                     print(f"Total con IVA: ${total_con_iva}")
#             case "4":
#                 print("Hasta luego!")
#                 break
#             case _:
#                 print("Opcion invalida")
# menu()

# def menu():
#     while True:
#         try:
#             print("Bienvenido/a al carrito de compras!")
#             print("1.- Ingresar nombre de usuario")
#             print("2.- Seleccionar productos disponibles")
#             print("3.- Sacar boleta de precios")
#             print("4.- Salir")
#             opcion = input("Seleccione una opcion: ")
#         except ValueError:
#             print("Error, seleccione una opcion valida")
        
#         match opcion:
#             case "1":
#                 nombre = input("Ingrese su nombre ")
#                 print(f"Hola {nombre}, bienvenido al carrito de compras")
#             case "2":
#                 print("Productos disponibles:")
#                 print("1.- Producto 1 - $3000")
#                 print("2.- Producto 2 - $2400")
#                 print("3.- Producto 3 - $1250")
#                 print("4.- Producto 4 - $5000")
#                 print("5.- Producto 5 - $1500")
#                 print("6.- Producto 6 - $2000")
#                 carrito = []
#                 while True:
#                     producto = input("Ingrese el numero del producto que desea comprar (o 'salir' para terminar): ")
#                     if producto == "salir":
#                         break
#                     elif producto in ["1", "2", "3", "4", "5", "6"]:
#                         carrito.append(producto)
#                         print(f"Agregado {producto} al carrito")
#                     else:
#                         print("Producto no valido")
#             case "3":
#                 if not carrito:
#                     print("El carrito esta vacio")
#                 else:
#                     total = 0
#                     for item in carrito:
#                         if item == "1":
#                             total += 3000
#                         elif item == "2":
#                             total += 2400
#                         elif item == "3":
#                             total += 1250
#                         elif item == "4":
#                             total += 5000
#                         elif item == "5":
#                             total += 1500
#                         elif item == "6":
#                             total += 2000
#                     iva = total * 0.21
#                     total_con_iva = total + iva
#                     print(f"Total de articulos comprados: {len(carrito)}")
#                     print(f"Total sin IVA: ${total}")
#                     print(f"IVA: ${iva}")
#                     print(f"Total con IVA: ${total_con_iva}")
#             case "4":
#                 print("Hasta luego!")
#                 break
#             case _:
#                 print("Opcion invalida")
# menu()

#pedir cantidad de alumnos
#pedir cantidad de notas por alumno
#promediar las notas de cada alumno y mostrar si aprobó o no
# bonus, mostrar el promedio de todos los alumnos ingresados
# sacar el promedio de cada alumno

while True:
    try:
        num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        if num_alumnos <= 0:
            print("La cantidad de alumnos debe ser mayor a 0.")
            continue
        break
    except ValueError:
        print("Error, ingrese un numero valido.")
alumnos = []
for i in range(num_alumnos):
    while True:
        try:
            num_notas = int(input(f"Ingrese la cantidad de notas para el alumno {i + 1}: "))
            if num_notas <= 0:
                print("La cantidad de notas debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error, ingrese un numero valido.")
    notas = []
    for j in range(num_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j + 1} del alumno {i + 1}: "))
                if nota < 0 or nota > 7:
                    print("La nota debe estar entre 0 y 7.")
                    continue
                break
            except ValueError:
                print("Error, ingrese una nota valida.")
        notas.append(nota)
    alumnos.append(notas)
promedios = []
for i, notas in enumerate(alumnos):
    promedio = sum(notas) / len(notas)
    promedios.append(promedio)
    if promedio >= 4:
        print(f"El alumno {i + 1} aprobó con un promedio de {promedio:.2f}.")
    else:
        print(f"El alumno {i + 1} no aprobó con un promedio de {promedio:.2f}.")
promedio_general = sum(promedios) / len(promedios)
print(f"El promedio general de todos los alumnos es: {promedio_general:.2f}.")



