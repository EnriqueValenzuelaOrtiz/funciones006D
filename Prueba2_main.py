import Prueba2 as p
#Código Principal

#Declarar Lista
lista_reservas=[]

opcion=0
while opcion!=6:
    #Mostrar Menú
    p.mostrar_menu()
    #Preguntamos Opción
    opcion = p.ingresar_opcion()

    if opcion==1:
        #Llamamos Función Agregar Reservas
        p.agregar_reserva(lista_reservas)
    
    elif opcion==2:
        #Solicitar Nombre
        nombre=input("Ingrese el nombre del huésped a buscar: \n")
        pos=p.buscar_reserva(lista_reservas, nombre)
        #Validamos
        if pos !=-1:
            #Mostramos los Datos
            print(f"Huésped: {lista_reservas[pos]["huesped"]}")
            print(f"Habitación: {lista_reservas[pos]["habitacion"]}")
            print(f"Noches: {lista_reservas[pos]["noches"]}")
            estado="Confirmado" if lista_reservas[pos]["confirmada"] else "Pendiente"
            print(f"Estado: {estado}")

        else:
            print(f"El husped {nombre} no ha sido encontrado")

    elif opcion==3:
         #Solicitar Nombre
        nombre=input("Ingrese el nombre del huésped a eliminar: \n")
        pos=p.buscar_reserva(lista_reservas, nombre)
        #Validamos
        if pos !=-1:
            #Elimino el elemnto de la Lista
            lista_reservas.pop(pos)
            print("Reserva eliminada correctamente")
        
        else:
            print(f"El husped {nombre} no ha sido encontrado")

    elif opcion==4:
        #Llamar Función Actualizar Confirmación
        p.confirmar_reservas(lista_reservas)
        print("Reservas actualizadas correctamente")

    elif opcion==5:
        p.confirmar_reservas(lista_reservas)
        p.mostrar_reservas(lista_reservas)

    elif opcion==6:
        print("Gracias por utilizar el sistema")
        


        