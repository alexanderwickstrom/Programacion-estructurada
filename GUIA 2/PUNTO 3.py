precio1 = float(input("Precio por Kg del producto 1: "))
kg1 = float(input("Cantidad Kg del producto 1: "))
precio2 = float(input("Precio por Kg del producto 2: "))
kg2 = float(input("Cantidad Kg del producto 2: "))
precio3 = float(input("Precio por Kg del producto 3: "))
kg3 = float(input("Cantidad Kg del producto 3: "))

total1 = precio1 * kg1
total2 = precio2 * kg2
total3 = precio3 * kg3
total = total1 + total2 + total3

print(f"Producto 1: ${total1:.2f}, Producto 2: ${total2:.2f}, Producto 3: ${total3:.2f}")
print(f"Total: ${total:.2f}")

if total > 100:
    total_descuento = total * 0.9
    print(f"Total con descuento del 10%: ${total_descuento:.2f}")
