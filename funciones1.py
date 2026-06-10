##Una tienda necesita mostrar la ficha de cada producto con su nombre, precio y stock
##Los datos cambian para cada product, pero el formato de presentación es simepre el mismo
##Crea una función con argumentos que reciba los datos del prducto y los muestre formateados sin retornar.

##------------------------------------------INICIALIZACIÓN----------------------------------------##

def datos_producto(name, stock, price):
    print("***********************")
    print("- Nombre del producto: {name} -")
    print("- Precio del producto: {price} -")
    print("- Stock del producto: {stock} -")
    print("***********************")

error="Error. Caracter inválido, inténtelo nuevamente."

##--------------------------------------ENTRADA----------------------------------------##

while True:
    try:
        name=input("Ingrese el nombre del prducto: \n")
        break

    except ValueError:
        print(error)
    
    
while True:
    try:
        price=int(input("Ingrese el precio del producto: \n"))
        
        if price<0:
            print(error)
        
        else:
            break
        break

    except ValueError:
        print(error)

while True:
    try:
        stock=int(input("Ingrese el stock del producto: \n"))
        
        if stock<0:
            print(error)
        
        else:
            break
        break

    except ValueError:
        print(error)

##----------------------------------------PROCESO--------------------------------------##

datos_producto()
