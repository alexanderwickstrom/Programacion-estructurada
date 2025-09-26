vendedores = []
ventas = []
for i in range(15):
    vendedores.append(input(f"Ingrese nombre del vendedor {i+1}: "))
    ventas.append(float(input(f"Ingrese venta en dólares del vendedor {i+1}: ")))

indice_max = ventas.index(max(ventas))
indice_min = ventas.index(min(ventas))
cambio = 140

print(f"Mayor venta: Vendedor {vendedores[indice_max]} - ${ventas[indice_max]:.2f} USD / ${ventas[indice_max]*cambio:.2f} ARS")
print(f"Menor venta: Vendedor {vendedores[indice_min]} - ${ventas[indice_min]:.2f} USD / ${ventas[indice_min]*cambio:.2f} ARS")
