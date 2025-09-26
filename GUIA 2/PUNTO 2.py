cantidad = int(input("Ingrese la cantidad de productos: "))
if cantidad < 5:
    print("No se permiten compras inferiores a 5 productos.")
elif 5 <= cantidad <= 15:
    print("El costo de envío es de $200.")
else:
    print("El envío es gratuito.")
