def stock_marca(stock):
    Mayuscula=False
    Minuscula=False
    for palabra in stock:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if Mayuscula==True or Minuscula==True:
            print("Marca ingresada correctamente")
            print[stock]
            return True
        else:
            print("Marca ingresada no encontrada.")
            return False
codigo="8475HD"
def valida_codigo(codigo):
    Mayuscula=False
    Minuscula=False
    Numero=False
    for passk in codigo:
        if passk.issuper():
            Mayuscula=True
        if passk.islower():
            Minuscula=True
        if passk.isdigit():
            Numero=True
        if Mayuscula and Minuscula and Numero==True:
            print("El código está bien escrito")
            return True
        else:
            print("Codigo incorrecto")
            return False

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

def mostrar_stock(dict):
    for key, stock in dict.items():
        print(key, stock)
def mostrar_productos(dict):
    for key, productos in dict.items():
        print(key, productos)

while True:
    try:
        print('''MENÚ PRODUCTOS ELECTRÓNICOS
                1. Stock marca.
                2. Búsqueda por precio.
                3. Actualizar precio.
                4. Salir.

''')
    except ValueError:
        print("Error, el valor ingresado no es válido")
    op=int(input("Seleccione una de las opciones: "))
    match op:
        case 1:
            marca=int(input("Ingrese marca que desea buscar: "))
            if marca==stock_marca(stock):
                print(f"El stock de la marca {marca} es: {stock[1][1]}")
                if stock[1][1]==0:
                    print("Objeto fuera de stock. Lo sentimos.")

        case 2:
            mostrar_orden_precio=sorted(stock.items(), key=lambda x: x[1], reverse=True)
            mostrar_stock(stock)
            mostrar_productos(productos)
            precio_min=int(input("Ingrese el precio minimo que busca: "))
            precio_max=int(input("Ingrese el precio máximo que busca "))
            if precio_max==0:
                print("Precio máximo inválido, este tiene que ser mayor a 0")
            for precio_min in range(mostrar_orden_precio) and precio_max in range(mostrar_orden_precio):
                print(mostrar_orden_precio)
            

        case 3:
            codigotry=int(input("Ingrese el código de stock que quiere cambiar el precio"))
            valida_codigo(codigo)
            if codigotry==valida_codigo(codigo):
                nuevo_precio=int(input("Ingrese el nuevo precio: "))
                stock[1][1]=nuevo_precio
                print(f"Precio actualizado a ${nuevo_precio}")
        case 4:
            print("Programa Finalizado.")
            break
        case _:
            print("Debe seleccionar una opción válida")
