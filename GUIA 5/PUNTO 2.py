matriz = [[],[],[],[]]

for i in range(0,4):
    for j in range(0,4):
        if i+j == 3:
            matriz[i].append(1)
        else:
            matriz[i].append(0)
    print(matriz[i])