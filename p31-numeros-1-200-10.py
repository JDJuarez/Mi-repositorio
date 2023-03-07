#Imprime numeros de 1 a 200 de 10 en 10 (continue)

import os

os.system('cls')
print('Imprime numeros de 1 a 200 de 10 en 10 (continue) \n')

c = 0

while c <= 200:
    c = c + 1
    if c % 10 != 0:
        continue
    print(c, end=' ')    