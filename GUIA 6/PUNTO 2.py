
suma = []


def aprobado():
    for i in range(3):
        nota = int(input(f'Ingrese la nota {i+1}: '))
        suma.append(nota)
    if sum(suma) > 12 and sum(suma) / 3 > 4:
        print('Aprobado.')
    else:
        print('No aprobado.')



aprobado()
