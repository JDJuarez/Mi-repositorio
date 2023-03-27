#Se desea imprimir los pares de 2 a n y su suma
#Dame número: 20 
#Salida: 2 4 6 8 10 12 14 16 18 20 , La suma es = xxx

import os

while True:
    os.system('cls')

    n = int(input('Hasta dónde n->? '))

    s=0

    for i in range(1, n+1):
        if i%2 == 0:
            s = s + i
            print(f'{i}', end= ' ')

    print(f', la suma es = {s}')

    res = input('\nDeseas continuar (S/N) ? ').upper()
    if res.upper()=='N':
        break

print('\nProceso terminado ...')