# Verificar si la suma de dos números es igual a un tercero
# n1=4, n2=5, n3=9  n1+n2=n3   n2+n3=n1   n1+n3=n2

import os

os.system('cls')
print('Verificar si la suma de dos números es igual a un tercero\n')
print('Dame 3 números enteros separados por espacio ? ')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n1 + n2 == n3:
    print('n1 + n2 = n3')
elif n2 + n3 == n1:
    print('n2 + n3 = n1')
elif n1 + n3 == n2:
    print('n1 + n3 = n2')
else:
    print('No hay sumas factibles')