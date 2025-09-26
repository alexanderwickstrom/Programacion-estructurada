
hermano1 = int(input("Ingrese la edad del primer hermano: "))
hermano2 = int(input("Ingrese la edad del segundo hermano: "))

def edadHermanos():
    diferencia = hermano1 - hermano2

    if hermano1 > hermano2:
        print("El hermano 1 es mayor.")
    
    else:
        print("El hermano 2 es mayor.")


    if diferencia < 0:
        diferencia = -diferencia
    
    print(f"La diferencia de edad es {diferencia}.")


edadHermanos()