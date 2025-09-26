edades = []
for _ in range(20):
    edades.append(int(input("Ingrese edad: ")))
print(f"Promedio de edad: {sum(edades)/len(edades):.2f}")
print(f"Edad más joven: {min(edades)}")
