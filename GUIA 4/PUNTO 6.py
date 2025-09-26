n = int(input("Ingrese cantidad de productos: "))
cantidades = []
costos = []

for i in range(n):
    cantidades.append(int(input(f"Ingrese cantidad del producto {i+1}: ")))
    costos.append(float(input(f"Ingrese costo del producto {i+1}: ")))

totales = [cantidades[i]*costos[i] for i in range(n)]
for i, total in enumerate(totales):
    print(f"Producto {i+1} - Total: ${total:.2f}")
    if total > 1000:
        print("  -> Supera $1000")
