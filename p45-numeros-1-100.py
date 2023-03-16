# Imprime números del 1 a 100
import os
os.system('cls')

n = int(input('Hasta donde ? '))
s = int(input('Paso        ? '))
for x in range(1,n + 1,s):
    print(x, end=' ')