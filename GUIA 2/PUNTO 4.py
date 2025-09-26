dni = input("Ingrese el DNI del empleado: ")
categoria = int(input("Ingresá la categoría del empleado (0-Maestranza, 1-Administración, 2-Gerencia): "))

if categoria == 0:
    nombre = "Maestranza"
    bruto = 23600
    jubilacion = bruto * 0.11
    obra_social = bruto * 0.03
    neto = bruto - jubilacion - obra_social
elif categoria == 1:
    nombre = "Administración"
    bruto = 35800
    jubilacion = bruto * 0.11
    obra_social = bruto * 0.05
    neto = bruto - jubilacion - obra_social
elif categoria == 2:
    nombre = "Gerencia"
    bruto = 60420
    jubilacion = bruto * 0.11
    obra_social = bruto * 0.05
    club = bruto * 0.04
    neto = bruto - jubilacion - obra_social - club
else:
    nombre = "Categoría inválida"
    neto = 0

print(f"DNI: {dni}, Categoría: {nombre}, Sueldo Neto: ${neto:.2f}")
