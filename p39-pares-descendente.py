# Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system('cls')
    p = 99
    suma = 0
    n = int(input('Los números pares desde 100 hasta el n ? '))
    while n<100:
        if n < 100:
            print('\nError ... Introduce un número mayor de 100.')
            n = int(input('\nLos números pares desde 100 hasta el n ? '))
    while(p < n):
        p = p + 1
        if p%2 == 0:
            print(p, end= ' ')
            suma = suma + p
    if p >= n:
        print(f'\n\nLa suma de los números pares es: {suma}')
        res = input('\nDeseas continuar (S/N) ? ')
        if res.upper()=='N':
            break

print('\nProceso terminado ...')