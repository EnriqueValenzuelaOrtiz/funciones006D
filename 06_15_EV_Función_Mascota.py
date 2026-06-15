def menu():
    print("******************************")
    print("------------MENÚ--------------")
    print("******************************")
    print("1.-Agreagar mascota")
    print("2.-Buscar mascota")
    print("3.-Eliiminar mascota")
    print("4.-Marcar cómo vendida")
    print("5.-Mostrar mascotas")
    print("6.-Salir")

def solicitar_opcion(opcion):
    while True:
        try:
            opcion=int(input("¿Qué desea hacer? \n"))

            if opcion<1 or opcion>6:
                print("Error. Ingrese un número válido")
            
            else:
                break
        
        except ValueError:
            print("Error. Ingrese un número entero")
    return opcion

datos_mascota=[]
op=0
while op!=6:
    menu()
    op=solicitar_opcion()