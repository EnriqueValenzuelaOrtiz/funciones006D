"""Desarrolla un programa en Python que implemente un sistema de gestión de reservas de un hotel, donde todo el                                                                        
comportamiento se organice mediante funciones bien definidas. El programa debe incluir un menú interactivo,                                                                               
validaciones de entrada, operaciones lógicas (decisiones y comparaciones) y uso de funciones separadas.                                                                                    

El sistema trabaja con una colección de reservas. Esta colección debe existir desde que el programa inicia y
estar disponible durante toda la ejecución. Cada vez que se agrega una reserva, se incorpora a esa colección
como un nuevo elemento.

Cada reserva se representa como un conjunto de campos asociados: huésped, habitación, noches y un indicador
de si está confirmada o no. La siguiente tabla resume los campos de cada registro

Cada diccionario se guarda dentro de una lista. La lista es la colección general; los diccionarios son las reservas
individuales dentro de ella. El programa comienza con la lista vacía y la va llenando a medida que se agregan
registros.

El sistema se controla desde un menú que aparece en pantalla cada vez que el usuario termina una acción. El
usuario elige una opción numérica, el programa ejecuta la tarea correspondiente y vuelve a mostrar el menú.
Esto se repite hasta que el usuario elige salir.

Para implementar este comportamiento debes definir dos funciones separadas: una que muestre las opciones en
pantalla (sin recibir nada ni retornar nada) y otra que lea y retorne la opción elegida por el usuario (sin recibir
nada, retornando el número validado). Ambas funciones deben invocarse en cada vuelta del ciclo.
"""

##--------------------------------------------------------------DEFINIMOS---------------------------------------------------------------##

#Función Menú
def mostrar_menu():
    print("****** Menú Principal******")
    print("1.- Agregar Reserva")
    print("2.- Buscar Reserva")
    print("3.- Eliminar Reserva")
    print("4.- Confirmar Reservas")
    print("5.- Mostrar Reservas")
    print("6.- Salir")
    print("***************************") 

#Función Opción Usuario
def ingresar_opcion():
    while True:
        try:
            op = int(input("Seleccione una opción: \n"))
            print("")
            if op < 1 or op > 6:
                raise ValueError
            
            else:
                return op
        
        except ValueError:
            print("Debe ingresar un número del 1 al 6")
            print("")
#Función Opción == 1 (Agregar Reserva)
def agregar_reserva(lista_r):
    while True:
        try:
            nombre_completo = input("Ingrese el nombre completo del Huesped: \n").strip()          
            print("")
            
            if nombre_completo !="" and nombre_completo.replace(" ","").isalpha():
                break
            
            else:
                raise ValueError
        
        except ValueError:
            print("Dijite un nombre válido")
            print("")
        
    """correcto = validar_huesped(nombre_completo)
    
    if not correcto:
        print("El nombre no puede estar vacío")
        return"""
    
    
    while True:
        try:
            numero_habitacion = input("Ingrese el número de habitación a reservar: \n").strip()
            print("")
            
            if numero_habitacion !="" and numero_habitacion.isdigit() and int(numero_habitacion)>=1 and int(numero_habitacion)<=200:
                break
                
            else:
                raise ValueError
        
        except ValueError:
            print("Error. Dijite un entero positivo entre 1 y 200")
            print("")
    
    while True:
        try:
            cant_noches = input("Ingrese la cantidad de noches a hospedarse: \n").strip()
            print("")
            
            if  cant_noches !="" and cant_noches.isdigit() and int(cant_noches)>0:
                break
            
            else:
                raise ValueError

        except ValueError:
            print("Error. Ingrese un número entero mayor a cero")
            print("")
    

    #Pasadas las Validaciones Agregamos al Diccionario
    reserva = {
        "huesped" : nombre_completo.strip().upper(),
        "habitacion": int(numero_habitacion),
        "noches": int(cant_noches),
        "confirmada": False
    }
    lista_r.append(reserva)
    print("Reserva agregada correctamente")

#Función Opción == 2 (Buscar Reserva)
def buscar_reserva(lista_r, huesped):
    #Recorremos la Lista
    for x in range(len(lista_r)):
        #Verificar si Existe Dentro de
        if huesped == lista_r[x]["huesped"]:
            return x   
    return -1

#Función Opción == 4 (Confirmar Reserva)
def confirmar_reservas(lista_r):
    #Recorremos la Lista
    for i in lista_r:
        #Buscamos Usuario con 2 o más noches reservadas
        if i["noches"] >= 2:
            i["confirmada"] = True
        else:
            i["confirmada"] = False
        #Confirmamos o Desmentimos

#Función Opción == 5 (Mostrar Reserva)
def mostrar_reservas(lista_r):
    print("======= Lista de Reservas =========")
    for i in lista_r:
        print(f"Huésped: {i["huesped"]}")
        print(f"Habitación: {i["habitacion"]}")
        print(f"Noches: {i["noches"]}")
        if i["confirmada"]:
            print("Estado: CONFIRMADA")
        else:
            print("Estado: PENDIENTE")
    print("===================================")

"""
#Funciones de validaciones
def validar_huesped(nombre):
    return nombre.strip() != 
    

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
"""

