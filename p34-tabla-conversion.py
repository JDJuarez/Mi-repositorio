# Imprimir una tabla de conversion de Peso a Dollar
import os

while(True):
    os.system('cls')
    tc = 18.00

    pi = float(input('Valor inicial: '))
    pf = float(input('Valor final  : '))

    c = pi

    print('\nPesos\tDolar')
    print('-'*15)

    while c <= pf:
        print(f'{c}\t{c/tc:.4f}')
        c += 1

    print('-'*15)

    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break