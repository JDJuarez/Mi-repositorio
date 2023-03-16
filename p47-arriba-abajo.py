#Imprimir números de 1 a n o de n a 1 según lo decida el usuario
import os

while(True):
    os.system('cls')
    print('[1] Números de 1 a n')
    print('[2] Números de n a 1')
    op = int(input('Elige    ? '))
    n  = int(input('Limite n ? '))

    if op == 1:
        print(f'\nImprimiendo números de 1 a {n}')
        for v in range(1,n+1):
            print(v, end=' ')
    elif op == 2:
        print(f'\nImprimiendo números de {n} hasta 1')
        for r in range(n,0,-1):
            print(r, end=' ')
    else:
        print('\nOpción invalida')

    res = input('\nDeseas Continuar (S/N) ? ').upper()
    if res == 'N': break

print('\n\nProceso terminado')