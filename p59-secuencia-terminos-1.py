#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:
#¿Cuántos términos?? 5 
#Salida: 1 + 1/2! + 1/3! + 1/4! + 1/5! , suma: aqui va la suma

import os

while True:
    os.system('cls')

    n = int(input('Número de renglones que el usuario desea n->? '))

    print(f'\nSalida: ',end=' ')
    s = 0
    print('1', end=' ')
    for i in range(1, n+1):
        if i != 1:
            print(f'1/{i}!', end=' ')
        
        if i != n:
            print(f'+', end=' ')
        
        f=1
        for j in range(1, i+1):
            f = f * j

        s = s + (1/f)
    print(f', suma: {s:.15f}')

    res = input('\nDeseas continuar (S/N) ? ').upper()
    if res.upper()=='N':
        break

print('\nProceso terminado ...')