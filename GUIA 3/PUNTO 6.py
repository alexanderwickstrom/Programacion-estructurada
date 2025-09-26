mejor_tiempo = None
vehiculo_mejor = None
for _ in range(12):
    num = input("Ingrese número de vehículo: ")
    tiempo = float(input("Ingresá tiempo en segundos: "))
    if mejor_tiempo is None or tiempo < mejor_tiempo:
        mejor_tiempo = tiempo
        vehiculo_mejor = num
print(f"Vehículo con mejor tiempo: {vehiculo_mejor}, Tiempo: {mejor_tiempo} segundos")
