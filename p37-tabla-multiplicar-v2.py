#Imprime las tablas desde 1 hasta n, desde 1 hasta m
import os

while(True):
    os.system('cls')

    n = int(input('Las tablas desde la tabla del 1 hasta la del n ? '))
    m = int(input('Desde 1 hasta m ? '))
    t = 1
    while t <= m:
        print(f'Tabla del {t}')
        
        c = 1
        while c <= n:
            print(f'{t} x {c} = {c*t}')
            c += 1
        print('\n')
        t += 1
        
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break

print('\nProceso terminado ...')
