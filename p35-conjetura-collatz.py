# Calcula los numeros de la conjetura de Collatz
import os
os.system('cls')

while(True):
    num = int(input('Dame un entero positivo ? '))

    while num != 1:
        print(num, end=' ')
        if num % 2 == 0:
            num = num//2
        else:
            num = num * 3 + 1
    print(num,end=' ')

    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break

print('\nProceso terminado ...')