# Imprime números del 100 a 1
import os
os.system('cls')

n = int(input('Desde donde ? '))
s = int(input('Retroceso        ? '))
for num in range(n,0,-s):
    print(num, end=' ')