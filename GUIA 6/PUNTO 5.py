def ordenar_numeros(a, b):
    if a > b:
        return b, a
    else:
        return a, b

a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))

menor, mayor = ordenar_numeros(a, b)
print(f"Los números ordenados de menor a mayor son: {menor}, {mayor}")
