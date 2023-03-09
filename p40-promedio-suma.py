#Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0, además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system('cls')
    print('La suma y el promedio de una serie de números, para poner fin introduce un 0.\nEmpieza introduciendo números con un enter:\n')
    b = True
    c = s = 0
    while b == True:
        n = float(input())
        if n == 0:
            p = s / c
            print(f'La suma de los números es             : {s}')
            print(f'La cantidad de números introducidos es: {c}')
            print(f'El promedio de los números es         : {p}')
        c = c + 1
        s = s + n
        if n == 0:
            b = False
    
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break
print('\nProceso terminado ...')