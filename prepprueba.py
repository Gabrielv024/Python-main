





def ingresa_juego(dict):
    while True:
        nombre = input("Ingrese el nombre del juego: ")
        if valida_nombre(nombre):
            break
        else:
            print("Error: Nombre inválido. Debe contener al menos un espacio y no puede comenzar o terminar con un espacio.")
    while True:
        try:
            precio = int(input("Ingrese el precio del juego: "))
            if valida_precio(precio):
                break
            else:
                print("Error: Precio inválido. Debe estar entre 8000 y 100000.")
        except ValueError:
            print("Error: Precio debe ser un número entero.")
    print("Ingrese el código del juego (debe tener 2 mayúsculas, 2 minúsculas y 4 números):")
    while True:
        code = input("Ingrese el código del juego: ")
        if valida_code(code):
            print("Inicio de ingreso")
            dict[len(dict) + 1] = {
                "nombre": nombre,
                "precio": precio,
                "codigo": code
            }
            print("Juego agregado correctamente.")
            break
        else:
            print("Error: Código inválido. No se agregó el juego.")

    nombre = input("Ingrese el nombre del juego: ")
    precio=int(input("Ingrese el precio del juego: "))
    while True:
        code=input("Ingrese el código del juego: ")
        if valida_code(code):
            print("Inicio de ingreso")
            print[list(dict.keys()[-1])]
            dict[list(dict.keys()[-1])+1]= {
                "nombre": nombre,
                "precio": precio,
                "codigo": code
            }
            print("Juego agregado correctamente.")
            break
        else:
            print("Error: Código inválido. No se agregó el juego.")

def valida_nombre(nombre):
    if nombre[-1]!= " " and nombre[0]!=" ":
        for l in nombre:
            if l==" ":
                return True
    else:
        return False



def valida_precio(precio):
    if precio>=8000 and precio<=100000:
        return True
    else:
        return False

def valida_code(clave):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in clave:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+=1
        if palabra.isdigit():
            Numero+=1
    if Mayuscula==2 and Minuscula==2 and Numero==4:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

valida_code()

def mostrar_juegos(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

def act_perros(dict):
    mostrar_juegos(dict)
    act=int(input("Seleccione el perro a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- Raza
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dict[act]["nombre"]=n
            case 2:
                n=input("ingrese la nueva raza")
                dict[act]["raza"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_code(n):
                    dict[act]["codigo"]=n
                else:
                    print("el paramatro del codigo no es correcto")
                    print('''
                    el codigo debe tener, una mayuscula, una minuscula, 
                    un numero y un largo exacto de 6''')
            case 4:
                break
            case _:
                    print("Opcion invalida")