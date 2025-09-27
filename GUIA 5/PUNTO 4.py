
import random


CANT = [[random.randint(0, 20) for j in range(15)] for i in range(50)]


TOTAL = [0] * 15
for j in range(15):
    for i in range(50):
        TOTAL[j] += CANT[i][j]


for v in range(15):
    print(f"Vendedor {v+1}: total={TOTAL[v]}")


mayor = max(TOTAL)
vendedor_top = TOTAL.index(mayor) + 1
print(f"\nEl vendedor con más ventas es el {vendedor_top}, con {mayor} artículos vendidos.")
