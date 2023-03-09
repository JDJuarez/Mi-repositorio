# Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir 0. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system('cls')
    print('El número mayor de una serie de números introducidos por el teclado, para poner fin introduce un 0.\n')
    print('Introduce números con enter:')
    b = True
    m = 0
    while b == True:
        n = float(input())
        if m < n:
            m = n
        if n == 0:
            print(f'El número mayor introducido es: {m}')
            b = False
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break
print('\nProceso terminado ...')