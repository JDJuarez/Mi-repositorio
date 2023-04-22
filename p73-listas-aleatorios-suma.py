# - Generar 2 listas de 10 números aleatorios
# - Suma ambas listas en una tercera, suma solo los elementos de cada lista si ambos son impares
# - Imprime las 3 listas

import random
import os

os.system('cls')

a = []
b = []
c = []

print('Los elementos aleatorios de la Lista 1: ')
for i in range(10):
    elemento = random.randint(1,100)
    a.append(elemento)
print(a)

print('Los elementos aleatorios de la Lista 2: ')
for i in range(10):
    elemento = random.randint(1,100)
    b.append(elemento)
print(b)

print('\nSuma de ambas listas, en lista 3, solo si los elementos son impares:')
for i in range(10):
    if((a[i]%2 != 0) and (b[i]%2 != 0)):
        elemento = a[i] + b[i]
        print(f'[{i+1}] {elemento}', end='')
        c.append(elemento)             
        
    else:
        print(f'[{i+1}] !', end='')
    if(i != 9):
        print(f',', end=' ')
print('\n\nLista 3:')
print(c)