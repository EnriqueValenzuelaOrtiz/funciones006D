#Funciones
#Mostrar menú
def mostrar_menu():
    print("****** Menú Principal******")
    print("1.- Agregar Reserva")
    print("2.- Buscar Reserva")
    print("3.- Eliminar Reserva")
    print("4.- Confirmar Reservas")
    print("5.- Mostrar Reservas")
    print("6.- Salir")
    print("*******************")
#Retornar la opcion del menu elegida por el usuario
def ingresar_opcion():
    while True:
        try:
            op = int(input("Seleccione una opción: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except ValueError:
            print("Debe ingresar un número del 1 al 6")
#Opcion 1
#Funcion para agregar
def agregar_reserva(lista_r):
    nombre_completo = input("Ingrese el nombre completo del Huesped: ")
    correcto = validar_huesped(nombre_completo)
    if not correcto:
        print("El nombre no puede estar vacío")
        return
    
    numero_habitacion = input("Ingrese el número de habitación a reservar: ")
    correcto = validar_habitacion(numero_habitacion)
    if not correcto:
        print("La habitación debe ser un número entero entre 1 y 200")
        return
    
    cant_noches = input("Ingrese la cantidad de noches a hospedarse: ")
    correcto = validar_noches(cant_noches)
    if not correcto:
        print("La cantidad de noches debe ser mayor a cero")
        return

    #agregamos al diccionario
    reserva = {
        "huesped" : nombre_completo.strip().upper(),
        "habitacion": int(numero_habitacion),
        "noches": int(cant_noches),
        "confirmada": False
    }
    lista_r.append(reserva)
    print("Reserva agregada correctamente")

#Opcion 2
def buscar_reserva(lista_r, huesped):
    #recorrer la lista
    for x in range(len(lista_r)):
        #verificar si existe dentro
        if huesped == lista_r[x]["huesped"]:
            return x
        
    return -1

#Opcion 4
def confirmar_reservas(lista_r):
    for i in lista_r:
        if i["noches"] >= 2:
            i["confirmada"] = True
        else:
            i["confirmada"] = False
#Opcion 5
def mostrar_reservas(lista_r):
    print(" ======= Lista de Reservas =========")
    for i in lista_r:
        print(f"Huésped: {i["huesped"]}")
        print(f"Habitación: {i["habitacion"]}")
        print(f"Noches: {i["noches"]}")
        if i["confirmada"]:
            print("Estado: CONFIRMADA")
        else:
            print("Estado: PENDIENTE")
        print("***************************")

#Funciones de validaciones
def validar_huesped(nombre):
    return nombre.strip() != ""

def validar_habitacion(hab):
    if hab.isdigit():
        validar = int(hab)
        return validar >= 1 and validar <= 200
    return False

def validar_noches(noches):
    if noches.isdigit():
        validar = int(noches)
        return validar > 0
    return False

#Código Principal