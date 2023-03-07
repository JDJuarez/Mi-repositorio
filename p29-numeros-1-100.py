#Imprime números de 1 a 100

import os

os.system('cls')

print('Imprime números de 1 a 100')
n = int(input('Hasta donde ? '))
m = int(input('Salto       ? '))

c = 1
while c<= n:
    print(c, end= ' ')
    c = c + m

print('\nProceso terminado ...')