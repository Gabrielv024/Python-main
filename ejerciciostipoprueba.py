# Ejercicio 1
def menu():
    total = 0
    passdescuento = "soyotaku"
    productos_comprados = 0
    intentosdescuento = 0
    while True:
        print("Bienvenido/a a nuestra pagina de delivery sushi")
        print("Este es nuestro menu de opciones!")
        op = int(input('''Ingrese una opcion: 
                 1.-Pikachu roll $4500
                 2.-Otaku roll $5000
                 3.-Pulpo venenoso roll $5200 
                 4.-Anguila Eléctrica roll $4800
                 5.- Salir
                '''))
        match op:
            case 1:
                print("Usted ha elegido Pikachu roll")
                print("El precio es de $4500")
                total += 4500
                productos_comprados += 1
            case 2:
                print("Usted ha elegido Otaku roll")
                print("El precio es de $5000")
                total += 5000
                productos_comprados += 1
            case 3:
                print("Usted ha elegido Pulpo venenoso roll")
                print("El precio es de $5200")
                total += 5200
                productos_comprados += 1
            case 4:
                print("Usted ha elegido Anguila Eléctrica roll")
                print("El precio es de $4800")
                total += 4800
                productos_comprados += 1
            case 5:
                if productos_comprados == 0:
                    print("No ha comprado nada")
                else:
                    print(f"El total de su compra es: ${total}")
                    print("El total de productos es: ", productos_comprados)               
                descinput= input("Si tiene un codigo de descuento, por favor ingrese: ")
                while descinput != passdescuento:
                    deserrortry = input("El codigo de descuento no es valido, por favor ingrese nuevamente: ")
                    intentosdescuento += 1
                    if intentosdescuento == 3:
                        print("Ha superado el maximo de intentos, no se aplicara el descuento")
                        print("El total de su compra es: ", total)
                        print("Gracias por su visita!")
                        break
                    elif deserrortry == passdescuento:
                        print("El total de su compra con descuento es: ", total * 0.9)
                        print("Gracias por su visita!")
                        break
                    elif descinput == passdescuento:
                        print("El total de su compra con descuento es: ", total * 0.9)
                        print("Gracias por su visita!")
                        break
            case _:
                print("Opción no válida, por favor intente nuevamente.") 

menu()



# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.

def menu_credito():
    saldo = 100000
    while True:
        print("Bienvenido/a a nuestro sistema de pago de tarjeta de crédito")
        print(f"Su saldo actual es: ${saldo}")
        op = int(input('''Ingrese una opcion: 
                 1.-Pago de Tarjeta de Crédito
                 2.-Simulación de Compras
                 3.-Salir
                '''))
        for i in range(1):
            if op == 1:
                print("Usted ha elegido Pago de Tarjeta de Crédito")
                print("El saldo actual es: ", saldo)
                pago = float(input("Ingrese el monto a pagar: "))
                if pago < 0:
                    print("El monto a pagar no puede ser menor a cero.")
                elif pago > saldo:
                    print("El monto a pagar no puede exceder el saldo actual.")
            elif op == 2:
                print("Usted ha elegido Simulación de Compras")
                print("El saldo actual es: ", saldo)
                compra = float(input("Ingrese el monto de la compra: "))
                if compra < 0:
                    print("El monto de la compra no puede ser menor a cero.")
                else:
                    saldo += compra
                    print(f"Compra realizada. Su nuevo saldo es: ${saldo}")
            elif op == 3:
                print("Gracias por su visita!")
                break
            else:
                print("Opción no válida, por favor intente nuevamente.")
        if op == 3:
            print("Gracias por su visita!")
            break
        if saldo < 0:
            print("Su saldo es negativo, por favor realice un pago.")
            break
menu_credito()

# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None
# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).
# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser necesario.

def menu_sesion():
    usuario1 = None
    usuario2 = None
    usuario3 = None
    contrasena1 = None
    contrasena2 = None
    contrasena3 = None
    while True:
        print("Bienvenido/a al sistema de inicio de sesión")
        op = int(input('''Ingrese una opcion: 
                 1.-Iniciar sesión
                 2.-Registrar usuario
                 3.-Salir
                '''))
        if op == 1:
            if usuario1 is None and usuario2 is None and usuario3 is None:
                print("No existen registros de usuarios, por favor registre un usuario antes.")
            else:
                print("Usted ha elegido Iniciar sesión")
                user = input("Ingrese su nombre de usuario: ")
                password = input("Ingrese su contraseña: ")
                if (user == usuario1 and password == contrasena1) or (user == usuario2 and password == contrasena2) or (user == usuario3 and password == contrasena3):
                    print("Inicio de sesión exitoso")
                    while True:
                        print("Bienvenido/a al menú principal")
                        op2 = int(input('''Ingrese una opcion: 
                                 1.-Realizar llamada
                                 2.-Enviar correo electrónico
                                 3.-Cerrar sesión
                                '''))
                        if op2 == 1:
                            print("Usted ha elegido Realizar llamada")
                            numero = input("Ingrese el número de celular (debe comenzar con 9 y tener 9 dígitos): ")
                            if len(numero) != 9 or numero[0] != '9':
                                print("Número inválido, debe comenzar con 9 y tener 9 dígitos.")
                            else:
                                print(f"Llamada realizada al número {numero}")
                        elif op2 == 2:
                            print("Usted ha elegido Enviar correo electrónico")
                            correo = input("Ingrese su correo electrónico: ")
                            while '@' not in correo:
                                correo = input("Correo inválido, por favor ingrese nuevamente: ")
                            mensaje = input("Ingrese el mensaje a enviar: ")
                            print(f"Correo enviado a {correo} con el mensaje: {mensaje}")
                        elif op2 == 3:
                            print("Cerrando sesión")
                            break
                        else:
                            print("Opción no válida, por favor intente nuevamente.")
                else:
                    print("Usuario o contraseña incorrectos, por favor intente nuevamente.")
        elif op == 2:
            print("Usted ha elegido Registrar usuario")
            if usuario1 is None:
                usuario1 = input("Ingrese su nombre de usuario: ")
                contrasena1 = input("Ingrese su contraseña: ")
            elif usuario2 is None:
                usuario2 = input("Ingrese su nombre de usuario: ")
                contrasena2 = input("Ingrese su contraseña: ")
            elif usuario3 is None:
                usuario3 = input("Ingrese su nombre de usuario: ")
                contrasena3 = input("Ingrese su contraseña: ")
            else:
                print("No se pueden registrar más usuarios.")
        elif op == 3:
            print("Gracias por su visita!")
            break


  


