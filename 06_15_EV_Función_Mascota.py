##---------------------------------------INICIALIZACIÓN--------------------------------------------##

#Función Menú
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
    print("******************************")


#Funión Opción
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

#Función Validación Nombre
def validar_nombre(nombre):
    
    return nombre.strip() != "" != int()

    """strip() -> eliminar todos los espacios en blanco al inicio y al final de un string y
    retorna True si es válido o False si no"""

#Función Validar Especie 
def validar_especie(especie):
    especies_validas = ["perro", "gato", "ave"]
    return especie.strip().lower() in especies_validas
    """<<return especie.strip().lower() in especies_validas>> entrega la variable <<especie>> 
    aserciorándose de que no tenga espacios en blanco, esté en minúscula y esté efectivamente
    en la lista de especies válidas, además, retorna True si lo consigue o False si no"""

#Función Validar Edad
def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0
    """"<<return edad.isdigit() and int(edad) > 0>> retorna edad sólo si <<edad>> contiene únicamente
    díjitos numéricos (utilizando .isdijit), además, se asegura de que sea un entero positivo (utilizando
    int(edad)), y tambien que sea mayor a cero"""

##----------------------------------------------PROCESO---------------------------------------------##

#Función Opción == 1 (Agregar Mascota)
def agregar_mascota(lista_m):
    
    #Solicitamos y Validamos Nombre
    nombre = input("Ingrese el nombre de su mascota: \n")
    correcta = validar_nombre(nombre)
    print("")
    if not correcta:
        print("El nombre no puede estar en blanco ni tener números")
        return
    
    #Solicitamos y Validamos Especie
    especie = input("Ingrese la especie (perro, gato o ave): \n")
    correcta = validar_especie(especie)
    print("")
    if not correcta:
        print("La especie solo puede ser perro, gato o ave")
        return
    
    #Solicitamos y Validamos Edad
    edad = input("Ingrese la edad de la mascota: \n")
    correcta = validar_edad(edad)
    print("")
    if not correcta:
        print("La edad debe ser un número entero mayor a cero")
        return
    
    #Pasadas las Validaciones, Agregar al Diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    
    #Agrego a la Lista
    lista_m.append(mascota)
    print("Mascota agregada correctamente")


##--------------------------------------------SALIDA---------------------------------------##

#Código Principal
datos_mascota=[]
op=0
while op!=6:
    menu()
    op=solicitar_opcion(op)

    if op == 1:
        agregar_mascota(datos_mascota)
    elif op == 2:
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sistema. Vuelva pronto")