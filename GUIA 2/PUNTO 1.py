def calcular_sueldo(categoria):
    if categoria == 1:
        sueldo = 32335
        jubilacion = sueldo * 0.11
        obra_social = sueldo * 0.03
        bono = sueldo * 0.08
        neto = sueldo - jubilacion - obra_social
        print(f"Sueldo Neto: ${neto:.2f}, Jubilación: ${jubilacion:.2f}, Obra Social: ${obra_social:.2f}, Bono compras: ${bono:.2f}")
    elif categoria == 2:
        sueldo = 38630.89
        jubilacion = sueldo * 0.11
        obra_social = sueldo * 0.03
        neto = sueldo - jubilacion - obra_social
        print(f"Sueldo Neto: ${neto:.2f}, Jubilación: ${jubilacion:.2f}, Obra Social: ${obra_social:.2f}")
    elif categoria == 3:
        sueldo = 45560.20
        jubilacion = sueldo * 0.11
        obra_social = sueldo * 0.03
        neto = sueldo - jubilacion - obra_social
        print(f"Sueldo Neto: ${neto:.2f}, Jubilación: ${jubilacion:.2f}, Obra Social: ${obra_social:.2f}")
    else:
        print("Categoría inválida.")

categoria = int(input("Ingresá la categoría del empleado (1-Repositor, 2-Cajero, 3-Supervisor): "))
calcular_sueldo(categoria)
