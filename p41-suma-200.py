#Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system('cls')
    print('La suma de números introducidos por el usuario hasta que la suma sea >= 200\n')
    b = True
    c = s = 0
    while b == True:
        n = float(input())
        c = c + 1
        s = s + n
        if s >= 200:
            b = False
            print(f'La suma de los números es             : {s}')
            print(f'La cantidad de números introducidos es: {c}')
    
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break
print('\nProceso terminado ...')