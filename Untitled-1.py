while True:
        try:
            numero_habitacion = input("Ingrese el número de habitación a reservar: \n").strip()
            print("")
            
            if numero_habitacion.isdigit() and numero_habitacion !=" "  and int(numero_habitacion)>=1 and int(numero_habitacion)<=200:
                break
                
            else:
                raise ValueError
        
        except ValueError:
            print("Error. Dijite un entero positivo entre 1 y 200")
            print("")