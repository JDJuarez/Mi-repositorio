# Imprimir pares e impares y su suma, segun lo decida el usuario 
import os
os.system('cls')

print('[P]ares de 1 a n y suma\n[I]mpares de 1 a n y su suma\n')
op = input('Opción ? ').upper()
n = int(input('Hasta dónde ? '))

s=0
if op=='P':
    print(f'\nNúmeros pares de 1 a {n} y su suma')
    for i in range(2,n+1, 2):
        print(i, end=' ')
        s += i
    
    print('\nSuma de pares ', s)
if op=='I':
    print(f'\nNúmeros impares de 1 a {n} y su suma')
    for i in range(1,n+1, 2):
        print(i, end=' ')
        s += i
    
    print('\nSuma de impares ', s)

print('\nproceso terminado')