import sys
import re
from Producto import Producto



#esta funcion sirve para printear los productos que tiene el diccionario
def menu_objeto(dicc):
    for i, j in sorted(dicc.items()):
        print("\n", j, "\n")


#este es un diccionario que tiene los productos de la tienda
diccSuper = {0:Producto("Jamon", 30, 50, 0),
            1:Producto("Merengue", 60, 20, 1),
            2:Producto("Jabon", 200, 10, 2),
            3:Producto("Mesa", 500, 10, 3),
            4:Producto("Silla", 100, 40, 4),
            5:Producto("Gato de juguete", 60, 30, 5),
            6:Producto("Leña", 90, 200, 6)
            }

#esto es el diccionario que se va a usar para guardar los productos que se van a comprar
diccCuenta = {}

#este es el menu, que tiene un .title() para que tenga mayusculas al principio de cada palabra
menu="""
1.- Agregar producto
2.- Remover producto
3.- añadir a cuenta
4.- retirar de la cuenta
5.- cobrar
6.- salir
""".title()

#bucle while para que el programa siga funcionando hasta que se le de la opcion de salir
while True:
    print("\n", menu)
    
    #se pide la opcion que se desea realizar y se valida que sea un numero del 1 al 6
    while True:
        inUser = input("Ingrese una opción del 1 al 6: ")
        #match sirve para validar que el input sea un numero
        match = re.match('^[1-6]$', inUser)
        if match:
            break
        print("Ingrese una opción incorrecta\n", menu)
        
    #se valida que la opcion sea correcta
    match int(inUser):
        case(1):
            print("\nAgregar producto\n".center(82, "-"))
            
            nombre = input("Ingrese el nombre del producto: ").lower()
            precio = input("Ingrese el precio del producto: ")
            cantidad =  input("Ingrese la cantidad del producto: ")
            
            #se valida que el precio y la cantidad sean numeros
            matchPrecio =re.match('^[0-9]+$', precio)
            matchCantidad = re.match('^[0-9]+$', cantidad)
            
            #si no son numeros te saca del case
            if matchPrecio and matchCantidad:
                
                #se valida que identificador no este repetido en las claves del diccionario
                for i in range(len(diccSuper.items())+1):
                    if i not in diccSuper.keys():
                        identificador = i
                        break
                    
                #se crea el objeto producto y se lo agrega al diccsuper
                diccSuper[identificador] = Producto(nombre, int(precio), int(cantidad), identificador)
                print("el ID del producto es: ", identificador)
            else:
                print("Ingrese un precio y cantidad correctos") 
        
        
        case(2):
            print("\nRemover producto\n".center(82, "-"))
            
            menu_objeto(diccSuper)
            
            #valida que el identificador sea un numero
            try:
                removedor = int(input("Ingrese el id del producto: "))
                
                #se valida que el id exista
                if removedor in sorted(list(diccSuper.keys())):
                    
                    #se elimina el producto del diccionario
                    diccSuper.pop(removedor)
                    print("El producto con el id: ", removedor, " ha sido removido")
                else:
                    print("id invalido")
            except:
                print("Ingrese un id correcto")  
                
        case(3):
            print("\nAñadir a la cuenta\n".center(84, "-"))
            
            menu_objeto(diccSuper)
            
            #valida que anadir y cantidad sean numeros
            try:
                anadir = int(input("Ingrese el id del producto que quiera llevarse: "))
                cantidad = int(input("Ingrese la cantidad del producto que quiera añadir: "))
                
                #se valida que el id exista y que la cantidad sea un numero positivo
                if anadir in sorted(list(diccSuper.keys())) and cantidad > 0:
                    
                    #se valida que la cantidad no sea mayor a la cantidad del producto
                    if diccSuper[anadir].cantidad - cantidad >=0:
                        diccSuper[anadir].cantidad -= cantidad
                        
                        #se valida que el identificador no este repetido en las claves del diccionario
                        if anadir in diccCuenta.keys():
                            #se suma la cantidad a la cantidad que ya tiene el producto
                            diccCuenta[anadir].cantidad += cantidad
                        else:
                            #se crea el objeto producto y se lo agrega a la cuenta
                            diccCuenta[anadir] = Producto(diccSuper[anadir].nombre, diccSuper[anadir].precio, cantidad, anadir)
                    else:
                        print("No hay suficiente cantidad")
                else:
                    print("id invalido o cantidad invalida")
            except:
                print("Ingrese una cantidad y id correctos")
                

        case(4):
            print("\nRetirar de la cuenta\n".center(86, "-"))
            
            menu_objeto(diccCuenta)
            
            #valida que cantidad y quitar sean numeros
            try:
                quitar = int(input("Ingrese el id del producto que quiera quitar de la cuenta: "))
                cantidad = int(input("Ingrese la cantidad del producto que quieras quitar: "))
                
                #se valida que el id exista y que la cantidad sea un numero positivo
                if quitar in sorted(list(diccCuenta.keys())) and cantidad > 0:
                    
                    #se valida que la cantidad no sea mayor a la cantidad del producto
                    if diccCuenta[quitar].cantidad - cantidad >=0:
                        diccCuenta[quitar].cantidad -= cantidad
                        diccSuper[quitar].cantidad += cantidad
                    else:
                        print("No hay suficiente cantidad")
                        
                #si no existe el id te saca del case
                if diccCuenta[quitar].cantidad <=0:
                    print("se a quitado este producto de la cuenta:",diccCuenta.pop(quitar))
            
            except:
                print("Ingrese una cantidad y id correctos")
                
                
        case(5):
            print("\nCobrar\n".center(72, "-"))
            
            menu_objeto(diccCuenta)
            total = 0
            
            #recorre el diccionario de la cuenta y suma el precio de cada producto por la cantidad
            for i, j in diccCuenta.items():
                total += j.precio * j.cantidad
            
            print("el total a pagar es de", total,"pesos")
            
        case(6):
            print("\nSalir\n".center(71, "-"))
            print("Gracias por su compra")
            sys.exit()