# Se desea imprimir los números de 1 a n de 10 en 10
#Dame número: 100 
#Salida. 1 11 21 31 41 51 61 71 81 91

import os

while True:
    os.system('cls')
    n = int(input('Hasta dónde n->? '))

    for i in range(1, n+1, 10):
        print(f'{i}', end= ' ')

    res = input('\nDeseas continuar (S/N) ? ').upper()
    if res.upper()=='N':
        break

print('\nProceso terminado ...')