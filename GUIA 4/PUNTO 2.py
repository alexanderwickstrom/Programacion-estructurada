n = int(input("Ingrese la cantidad de notas: "))
notas = []
for _ in range(n):
    notas.append(float(input("Ingrese nota: ")))

aprobados = sum(1 for x in notas if x >= 6)
desaprobados = sum(1 for x in notas if x < 6)

print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de desaprobados: {desaprobados}")
