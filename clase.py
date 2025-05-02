# intentos=3
# clave=3344
# password=int(input("Ingrese su pass: "))
# while clave!=password and intentos==2:
#     print("Error, clave invalida")
#     intentos=intentos+1
#     print(intentos)
#     password=int(input("ingrese su pass:"))
    
#     if intentos>=3:
#         print("Ya no tiene mas intentos")
#     else:
#         print("Bienvenido al sistema")


# import random

# numAzar=random.randint(1,30)

# print(numAzar)
# if numAzar>=20:
#     print("Puede pasar")
# else:
#     print("Le falta puntaje")

# import random


# numaadivinar=random.randint(1,50)

# num=int(input("Adivine el numero:"))

# while numaadivinar!=num:
#     print(numaadivinar)
#     if num>numaadivinar:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     num=int(input("Adivine el numero:"))
# print("Felicitaciones, adivinaste el numero")


# import random

# barril=random.randint(1,6)
# rul=int(input("Disparo :"))

# while barril!=rul:
#     print("Disparo fallido")
#     rul=int(input("Disparo :"))
# print("Disparo exitoso")
# print("Fin del juego")
   
# import random
# j1=0
# j2=0
# meta=20
# turno=1
# dado=random.randint(1,6)
# while j1<meta and j2<meta:
#     if turno%2==0:
#         print("Turno de jugador 1")
#         j1=j1+dado
#         print("Jugador 1 avanza",j1)
#         if j1>=20:
#             print("Jugador 1 gana")
#             break
#         turno=1 
#     else:
#         print("Turno de jugador 2") 
#         j2=j2+dado
#         print("Jugador 2 avanza",j2)
#         if j2>=20:
#             print("Jugador 2 gana")
#             break
#         turno=2
    
# print("Fin del juego")
# print("Jugador 1:",j1)
# print("Jugador 2:",j2)

# arancel=200000
# descuento=0

# print("Bienvenido al sistema de descuentos")
# print("Comunas disponibles para el descuento:")
# print("1. La Florida 20%")
# com1=1
# print("2. Puente Alto 30%")
# com2=2
# print("3. La Pintana 25%")
# com3=3
# print("4. San Joaquin 15%")
# com4=4
# print("5. No tiene descuento")
# nodesc=5
# print("6. Salir")
# salida=6
# comuna=int(input("Ingrese su comuna:"))
# if comuna==com1:
#     print("La Florida")
#     descuento=0.20*arancel
#     print("El descuento es de:",descuento)
# elif comuna==com2:
#     print("Puente Alto")
#     descuento=0.30*arancel
#     print("El descuento es de:",descuento)
# elif comuna==com3:
#     print("La Pintana")
#     descuento=0.25*arancel
#     print("El descuento es de:",descuento)
# elif comuna==com4:
#     print("San Joaquin")
#     descuento=0.15*arancel
#     print("El descuento es de:",descuento)
# elif comuna==nodesc:
#     print("No tiene descuento")
# elif comuna==salida:
#     print("Gracias por usar el sistema")
#     descuento=0
# total=arancel-descuento/100

# grupofam=int(input("Ingrese la cantidad de familiares que viven con usted:"))
# if grupofam==1:
#     print("Grupo familiar: 1")
#     descuento=0.01+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==2:
#     print("Grupo familiar: 2")
#     descuento=0.02+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==3:
#     print("Grupo familiar: 3")
#     descuento=0.03+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==4:   
#     print("Grupo familiar: 4")
#     descuento=0.04+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==5:
#     print("Grupo familiar: 5")
#     descuento=0.05+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==6:
#     print("Grupo familiar: 6")
#     descuento=0.06+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==7:
#     print("Grupo familiar: 7")
#     descuento=0.07+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==8:
#     print("Grupo familiar: 8")
#     descuento=0.08+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==9:
#     print("Grupo familiar: 9")
#     descuento=0.09+descuento*arancel
#     print("El descuento es de:",descuento)
# elif grupofam==10:
#     print("Grupo familiar: 10")
#     descuento=0.10+descuento*arancel
#     print("El descuento es de:",descuento)
#     total=arancel-descuento
# else:
#     print("No tiene descuento")
#     total=arancel-descuento/100
# print("El total a pagar es:",total)



# caja1=50000
# caja2=100000
# caja3=200000
# billetes1=10
# billetes2=10
# billetes3=10

# print("Bienvenido al cajero automatico")
# print("1. Depositar")
# print("2. Retirar")
# print("3. Consultar saldo")
# print("4. Salir")
# opcion=int(input("Ingrese la opcion deseada:"))
# if opcion==1:
#     print("Depositar")
#     print("1. Depositar en caja 1")
#     print("2. Depositar en caja 2")
#     print("3. Depositar en caja 3")
#     caja=int(input("Ingrese la caja donde desea depositar:"))
#     if caja==1:
#         deposito=int(input("Ingrese el monto a depositar:"))
#         if deposito<=billetes1*10000:
#             caja1=caja1+deposito
#             billetes1=billetes1-deposito/10000
#             print("Deposito exitoso")
#             print("Saldo disponible:",caja1)
#         else:
#             print("No hay suficientes billetes disponibles")
#     elif caja==2:
#         deposito=int(input("Ingrese el monto a depositar:"))
#         if deposito<=billetes2*20000:
#             caja2=caja2+deposito
#             billetes2=billetes2-deposito/20000
#             print("Deposito exitoso")
#             print("Saldo disponible:",caja2)
#         else:
#             print("No hay suficientes billetes disponibles")
#     elif caja==3:
#         deposito=int(input("Ingrese el monto a depositar:"))
#         if deposito<=billetes3*50000:
#             caja3=caja3+deposito
#             billetes3=billetes3-deposito/50000
#             print("Deposito exitoso")
#             print("Saldo disponible:",caja3)
#         else:
#             print("No hay suficientes billetes disponibles")
#     else:
#         print("Opcion invalida")
# elif opcion==2:
#     print("Retirar")
#     print("1. Retirar de caja 1")
#     print("2. Retirar de caja 2")
#     print("3. Retirar de caja 3")
#     caja=int(input("Ingrese la caja donde desea retirar:"))
#     if caja==1:
#         retiro=int(input("Ingrese el monto a retirar:"))
#         if retiro<=caja1:
#             caja1=caja1-retiro
#             billetes1=billetes1+retiro/10000
#             print("Retiro exitoso")
#             print("Saldo disponible:",caja1)
#         else:
#             print("No hay suficientes fondos disponibles")
#     elif caja==2:
#         retiro=int(input("Ingrese el monto a retirar:"))
#         if retiro<=caja2:
#             caja2=caja2-retiro
#             billetes2=billetes2+retiro/20000
#             print("Retiro exitoso")
#             print("Saldo disponible:",caja2)
#         else:
#             print("No hay suficientes fondos disponibles")
#     elif caja==3:
#         retiro=int(input("Ingrese el monto a retirar:"))
#         if retiro<=caja3:
#             caja3=caja3-retiro
#             billetes3=billetes3+retiro/50000
#             print("Retiro exitoso")
#             print("Saldo disponible:",caja3)
#         else:
#             print("No hay suficientes fondos disponibles")
#     else:
#         print("Opcion invalida")
# elif opcion==3:
#     print("Consultar saldo")
#     print("1. Consultar saldo de caja 1")
#     print("2. Consultar saldo de caja 2")
#     print("3. Consultar saldo de caja 3")
#     caja=int(input("Ingrese la caja que desea consultar:"))
#     if caja==1:
#         print("Saldo disponible:",caja1)
#     elif caja==2:
#         print("Saldo disponible:",caja2)
#     elif caja==3:
#         print("Saldo disponible:",caja3)
#     else:
#         print("Opcion invalida")
# elif opcion==4:
#     print("Gracias por usar el cajero automatico")
# else:
#     print("Opcion invalida")

# import time
# import random

# j1=0
# j2=0
# meta=30
# turno=random.randint(1,2)
# dado=random.randint(1,6)
# while j1<meta and j2<meta:
#     if turno%2==0:
#         print("Turno de jugador 1")
#         dado=random.randint(1,6)
#         j1=j1+dado
#         print("Jugador 1 avanza",j1)
#         if j1>=30:
#             print("Jugador 1 gana")
#             break
#         turno=1 
#     else:
#         print("Turno de jugador 2") 
#         dado=random.randint(1,6)
#         j2=j2+dado
#         print("Jugador 2 avanza",j2)
#         if j2>=30:
#             print("Jugador 2 gana")
#             break
#         turno=2
#     time.sleep(1)
# print("Fin del juego")
# print("Jugador 1:",j1)
# print("Jugador 2:",j2)

#Clasificar segun categoria y precio
#cat 1 +200, cat 2 +400, cat 3 +600
#precios : 1000 y menos;3% entre 1001 y 5000; 5%, 5001 y mas %6
#poner listado de 3 productos por categoria, las cat son 1 ,2 y 3
#agregar los impuestos al precio, segun la cat y luego aplicar el descuento al total de la boleta segun el monto total

print("Bienvenido al sistema de clasificacion de productos")
print("1. Agua Mineral")
print("2. Galletas")
print("3. Jugo")
num=int(input("Ingrese el numero del producto:"))
if num==1:
    print("Agua Mineral")
    precio=1000
    print("Precio:",precio)
    print("1. Categoria 1")
    print("2. Categoria 2")
    print("3. Categoria 3")
    cat=int(input("Ingrese la categoria:"))
    if cat==1:
        precio=precio+200
        print("Categoria 1")
        print("Precio:",precio)
        if precio<=1000:
            descuento=0.03*precio
            total=precio-descuento
            print("El total a pagar es:",total)
        elif precio>1000 and precio<=5000:
            descuento=0.05*precio
            total=precio-descuento
            print("El total a pagar es:",total)
        elif precio>5000:
            descuento=0.06*precio
            total=precio-descuento
            print("El total a pagar es:",total)
    elif cat==2:
        precio=precio+400
        print("Categoria 2")
        print("Precio:",precio)
        if precio<=1000:
            descuento=0.03*precio
            total=precio-descuento
            print("El total a pagar es:",total)
        elif precio>1000 and precio<=5000:
            descuento=0.05*precio
            total=precio-descuento
            print("El total a pagar es:",total)
        elif precio>5000:
            descuento=0.06*precio
            total=precio-descuento
            print("El total a pagar es:",total)
    elif cat==3:
        precio=precio+600
        print("Categoria 3")
        print("Precio:",precio)
        if precio<=1000:
            descuento=0.03*precio
            total=precio-descuento
            print("El total a pagar es:",total)
        elif precio>1000 and precio<=5000:
            descuento=0.05*precio
            total=precio-descuento
            print("El total a pagar es:",total)
        elif precio>5000:
            descuento=0.06*precio
            total=precio-descuento
            print("El total a pagar es:",total)







