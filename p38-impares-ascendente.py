#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n), además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el usuario lo decida.
import os

while(True):
    os.system('cls')
    i = suma = 0
    n = int(input('Los números impares de forma ascendente desde 1 hasta el n ? '))
    while(i < n):
        i = i + 1
        if i%2 != 0:
            print(i, end= ' ')
            suma = suma + i
    if i >= n:
        print(f'\n\nLa suma de los números impares es: {suma}')
        res = input('\nDeseas continuar (S/N) ? ')
        if res.upper()=='N':
            break

print('\nProceso terminado ...')