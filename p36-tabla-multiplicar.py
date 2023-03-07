#Imprime la tabla de multiplicar que el usuario pida de 1 a n
import os

while(True):
    os.system('cls')
    t = int(input('Que tabla quieres      ? '))
    n = int(input('hasta dónde la quieres ? '))

    c = 1
    while c <= n:
        print(f'{c} x {t} = {c*t}')
        c += 1
        
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break

print('\nProceso terminado ...')