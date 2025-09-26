for _ in range(5):
    dni = input("Ingrese el DNI del cliente: ")
    servicio = int(input("Ingrese el tipo de servicio (1-30Mb, 2-50Mb, 3-100Mb): "))
    if servicio == 1:
        monto = 750
    elif servicio == 2:
        monto = 1100
    elif servicio == 3:
        monto = 1500 * 0.95
    else:
        monto = 0
    print(f"DNI: {dni}, Servicio: {servicio}, Monto a pagar: ${monto:.2f}")
