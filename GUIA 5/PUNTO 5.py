
matriz = [[0]*4 for _ in range(4)]

for i in range(4):
    for j in range(3):
        matriz[i][j] = int(input(f"Ingrese nota {j+1} del alumno {i+1}: "))
    matriz[i][3] = sum(matriz[i][0:3]) / 3

print("\nNotas y promedios:")
for i in range(4):
    print(f"Alumno {i+1}: {matriz[i][0:3]} → Promedio = {matriz[i][3]:.2f}")
