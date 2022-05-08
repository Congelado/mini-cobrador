import re
from Grupo import Grupo



def menu_objeto(dicc):
    for i, j in sorted(dicc.items()):
        print("\n", j, "\n")



diccSuper = {}
diccCuenta = {}

menu="""
1.- Agregar producto
2.- Remover producto
3.- añadir a cuenta
4.- retirar de la cuenta
5.- cobrar
6.- salir
""".title()

while True:
    print("\n", menu)
    while True:
        inUser = input("Ingrese una opción del 1 al 6: ")
        match = re.match(r'^[1-6]$', inUser)
        if match:
            break
        print("Ingrese una opción incorrecta\n", menu)
        

    match int(inUser):
        case(1):
            print("\nAgregar producto\n".center(82, "-"))
            
            nombre = input("Ingrese el nombre del producto: ").lower()
            precio = int(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            
            for i in range(len(diccSuper.items())+1):
                if i not in diccSuper.keys():
                    identificador = i
                    break
                
            diccSuper[identificador] = Grupo(nombre, precio, cantidad, identificador)
            print("el ID del producto es: ", identificador)
            
        case(2):
            print("\nRemover producto\n".center(82, "-"))
            
            menu_objeto(diccSuper)
            
            try:
                removedor = int(input("Ingrese el id del producto: "))
            except:
                pass
            
            if removedor in sorted(list(diccSuper.keys())):
                diccSuper.pop(removedor)
                print("El producto con el id: ", removedor, " ha sido removido")
            else:
                print("id invalido")
        
            
        case(3):
            print("\nAñadir a la cuenta\n".center(84, "-"))
            
            menu_objeto(diccSuper)
            
            try:
                anadir = int(input("Ingrese el id del producto que quiera llevarse: "))
                cantidad = int(input("Ingrese la cantidad del producto que quiera añadir: "))
            except:
                pass
            diccSuper[anadir].cantidad -= cantidad
            diccCuenta[anadir] = Grupo(diccSuper[anadir].nombre, diccSuper[anadir].precio, cantidad, anadir)
            
            
        case(4):
            print("\nRetirar de la cuenta\n".center(86, "-"))
            
            menu_objeto(diccCuenta)
            try:
                quitar = int(input("Ingrese el id del producto que quiera qujitar de la cuenta: "))
                cantidad = int(input("Ingrese la cantidad del producto que quieras quitar: "))
            except:
                pass
            diccCuenta[quitar].cantidad -= cantidad
            if diccCuenta[quitar].cantidad == 0 or diccCuenta[quitar].cantidad < 0:
                print("se a quitado este producto de la cuenta:",diccCuenta.pop(quitar))
                
        case(5):
            print("\nCobrar\n".center(72, "-"))
            
            menu_objeto(diccCuenta)
            total = 0
            
            for i, j in diccCuenta.items():
                total += j.precio * j.cantidad
            
            print("el total a pagar es de", total,"pesos")
            
        case(6):
            print("\nSalir\n".center(71, "-"))
            break