total_personas = 0
total_varones = 0
total_mujeres = 0
varones_16_65 = 0
mayor_edad = 0
datos_mayor = ()

while True:
    dni = int(input("Ingrese número de documento (0 para terminar): "))
    if dni == 0:
        break
    edad = int(input("Ingresá edad: "))
    sexo = input("Ingresá sexo (F/M): ").upper()
    total_personas += 1
    if sexo == "M":
        total_varones += 1
        if 16 <= edad <= 65:
            varones_16_65 += 1
    elif sexo == "F":
        total_mujeres += 1
    if edad > mayor_edad:
        mayor_edad = edad
        datos_mayor = (dni, edad, sexo)

porcentaje_varones = (varones_16_65 / total_varones * 100) if total_varones > 0 else 0

print(f"Total de personas: {total_personas}")
print(f"Total varones: {total_varones}")
print(f"Total mujeres: {total_mujeres}")
print(f"% de varones entre 16 y 65: {porcentaje_varones:.2f}%")
print(f"Persona con mayor edad: DNI: {datos_mayor[0]}, Edad: {datos_mayor[1]}, Sexo: {datos_mayor[2]}")
