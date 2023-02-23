#Calcula la paga de un trabajdador considerando 40 horas la jornada, las horas extra se pagan al doble

import os

os.system('cls')
print('Calcula la paga de un trabajador considerando horas extra ( se pagan al doble)\n')
nombre = input('Dame tú nombre ? ')
horas = int(input('Horas trabajadas ? '))
paga = float(input('Paga por hora ? '))

if horas > 40:
    extra = horas -40
    total = (40*paga) + (extra * 2 * paga)
    print(f'Horas extra: {extra}')
else:
    total = horas * paga

print(f'\n {nombre} trabajo {horas} horas, con una paga de {paga} pesos, total del pago {total} pesos')