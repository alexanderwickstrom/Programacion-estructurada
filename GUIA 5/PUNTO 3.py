import random

notas = [[random.randint(1, 10) for j in range(5)] for i in range(40)]

for i in range(40):
    promedio = sum(notas[i]) / 5
    print(f"Alumno {i+1}: notas={notas[i]} promedio={promedio:.2f}")
