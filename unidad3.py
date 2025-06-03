# numero = int(input("Ingrese valor: "))

# while True:
#     try:
#         if numero < 20 or numero > 50:
#             print("El número no está en el rango de 20 a 50.")
#         else:
#             print("Numero ingresado correctamente.")
#     except ValueError:
#         print("Por favor, ingrese un número válido.")


#     for i in range (numero):
#         print("algo")   


#     lista = [1, 2, 3, 4, 5]
#     lista.append(6)
#     for elemento in lista:
#         print(elemento)

#     milista = [1, 2, 3, 4, 5]
#     milista.insert(3, "juan")

#     for elemento in milista:
#         print(elemento)

#     milistaa = [1, 2, 3,"Juan" ,4, 5]
#     milistaa.remove("Juan")

#     #si borro el 2 para removerlo tendria q poner milistaa.remove(1) ya que empieza desde 0

#     milistaaaa= [1, 2, 3,"Joan" ,4, 5]
#     milistaaaa.reverse() #invirte la lista
#     milistaaaa.sort()  #ordena la lista de menor a mayor



    
#     #1 agregar un producto
#     #2 eliminar un producto
#     #3 ver todos los productos en orden de precios
#     #4 salir
#     lista_prodructos = []
#     print("Bienvenido/a a la lista de productos")
#     while True:
#         try:
#             print("1.- Agregar un producto")
#             print("2.- Eliminar un producto")
#             print("3.- Ver todos los productos en orden de precios")
#             print("4.- Salir")
#         except ValueError:
#             opc=int(input("Seleccione una opcion"))
#         if opc== 1:
#             while True:
#                 try:
#                     print("Lista de productos disponibles")
#                     print(''' 
#                         1.- Rp $10000
#                         2.- V-Bucks $5000
#                         3.- Robux $5500
#                         4.- PSN $11000 
#                         5.- Xbox GPass $10900
#     ''')
#                 except ValueError:

#                     opcprdct=int(input("Seleccione una opcion"))
#                 if 

def validar_numero(minimo_maximo_texto):
       while True:
              try:
                     aux = int(input(f"Ingrese {texto}: "))



from os import system
lista_productos = []
while True:
        print("Bienvenido/a a la lista de productos")
        print("1.- Agregar un producto")
        print("2.- Eliminar un producto")
        print("3.- Ver todos los productos en orden de precios")
        print("4.- Salir")

        opc=int(input("Seleccione una opcion"))
        match opc:
            case 1:
                    producto=int(input("Ingrese un producto: "))
                    lista_productos.append(producto)
                    print(f"El producto {producto} fue agregado correctamente!")
                    input("Presione enter para continuar...")
                    system("cls")
                
            case 2:
                    print("=======================")
                    print("====== PRODUCTOS ======")
                    print("=======================")
                    cont = 1
                    for i in lista_productos:
                            print(f"{cont}.- {i}")
                            cont+=1

                    aux = int(input("Cual desea eliminar "))-1
                    lista_productos.pop(aux)
                    input("Presione enter para continuar...")
                    system("cls")
            case 3:
                print("=======================")
                print("====== PRODUCTOS ======")
                print("=======================")
                cont = 1
                for i in lista_productos:
                       print(f"{cont} .- {i}")
                       cont+=1
            case 4:
            
            case _:
                      print("Opcion invalida, intente de nuevo")
                        