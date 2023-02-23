#Verifica si la suma de dos números es igual a un tercer

import os

os.system('cls')

print('Verifica si la suma de dos números es igual a un tercer\n')
print('Dame 3 números separados por Enter ?\n')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print('Son iguales')
else:
    print('Son diferentes')

print('\nProceso Terminado')