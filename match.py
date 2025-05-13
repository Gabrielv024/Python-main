#Explicacion y uso de match

def suma():
    n1=int(input("Ingrese un numero:"))
    n2=int(input("Ingrese otro numero: "))
    print("El resultado de la suma es: ",n1+n2)
    suma()
def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("El resultado de la resta es: ",n1-n2)
    resta()
def multiplicacion():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("El resultado de la multiplicacion es: ",n1*n2)
    multiplicacion()
def division():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("El resultado de la division es: ",n1/n2)
    division()
    try:
        n1=int(input("Ingrese un numero: "))
        n2=int(input("Ingrese otro numero: "))
        print("El resultado de la division es: ",n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        print(f"Se produjo una excepcion: {nombre_de_excepcion}")


def calcu():
    while True:
     op=int(input('''Ingrese una opcion: 
                1.- Suma
                2.- Resta
                3.- Multiplicacion
                4.- Division
                5.- Salir
                '''))

     match op:
        case 1:
            print("Suma")
            suma()
        case 2:
            print("Resta")  
            resta() 
        case 3:
            print("Multiplicacion")
            multiplicacion()
        case 4:
            print("Division")
            division()
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")
calcu()


#Nuevo menu recursivo. debe tener 3 programas creados anteriormente el menu debe llamar a estos programas y ejecutarlos de manera correcta debe tener la opcion de salir y la opcion por defecto

def promedio():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    n3=int(input("Ingrese otro numero: "))
    print("El promedio es: ",(n1+n2+n3)/3)
    promedio()
def factorial():
    n=int(input("Ingrese un numero: "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("El factorial es: ",fact)
    factorial()
def potencia():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print("La potencia es: ",n1**n2)
    potencia()

def menu():
    while True:
     op=int(input('''Ingrese una opcion: 
                1.- Promedio
                2.- Factorial
                3.- Potencia
                4.- Salir
                '''))

     match op:
        case 1:
            print("Promedio")
            promedio()
        case 2:
            print("Factorial")  
            factorial() 
        case 3:
            print("Potencia")
            potencia()
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")
menu()

def numazar():
    import random
    numAzar=random.randint(1,30)

    print(numAzar)
    if numAzar>=20:
        print("Puede pasar")
    else:
        print("Le falta puntaje")

    import random


    numaadivinar=random.randint(1,50)

    num=int(input("Adivine el numero:"))

    while numaadivinar!=num:
        print(numaadivinar)
        if num>numaadivinar:
            print("El numero a adivinar es menor")
        else:
            print("El numero a adivinar es mayor")
        num=int(input("Adivine el numero:"))
    print("Felicitaciones, adivinaste el numero")
numazar()
