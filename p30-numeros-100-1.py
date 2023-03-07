#Imprime números de 100 a 1

import os

os.system('cls')

print('Imprime números de 100 a 1: \n')
n = int(input('Hasta donde ? '))
m = int(input('Salto       ? '))

c = n
while c>= 0:
    print(c, end= ' ')
    c = c - m

print('\nProceso terminado ...')