total_socios = int(input("Ingrese cantidad de socios: "))
tenis = 0
futbol = 0
suma_edades = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
cantidad_deporte = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for _ in range(total_socios):
    numero = input("Número de socio: ")
    edad = int(input("Edad: "))
    deporte = int(input("Tipo de deporte (1-Tenis,2-Rugby,3-Voley,4-Hockey,5-Fútbol): "))
    suma_edades[deporte] += edad
    cantidad_deporte[deporte] += 1
    if deporte == 1:
        tenis += 1
    elif deporte == 5:
        futbol += 1

print(f"Socios que practican tenis: {tenis}")
print(f"Socios que practican fútbol: {futbol}")
for d in suma_edades:
    if cantidad_deporte[d] > 0:
        promedio = suma_edades[d] / cantidad_deporte[d]
        print(f"Promedio de edad deporte {d}: {promedio:.2f}")
