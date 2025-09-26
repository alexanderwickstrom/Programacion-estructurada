tipoTriangulo = []

def cargar_valores():
    entrada = input("Ingresá los lados del triángulo (separados por comas o espacios): ")
    entrada = entrada.replace(",", " ")
    partes = entrada.split()

    if len(partes) != 3:
        print("Debes ingresar exactamente 3 valores.")
        return

    for p in partes:
        try:
            tipoTriangulo.append(int(p))
        except ValueError:
            print("Todos los lados deben ser números enteros.")
            return

    clasificar_triangulo(tipoTriangulo)

def clasificar_triangulo(lados):
    a, b, c = lados

    if a + b <= c or a + c <= b or b + c <= a:
        print("Los lados ingresados no forman un triángulo válido.")
        return

    if a == b == c:
        print("Es un triángulo equilátero.")
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")

cargar_valores()
