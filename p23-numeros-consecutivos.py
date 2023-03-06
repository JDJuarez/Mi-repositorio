#Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son (1,4,6) mandar mensaje de error.

import os

os.system('cls')
print('Dame tres números enteros separados con un espacio: \n')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n1 + 1 == n2:
    if n2 + 1 == n3:
        print('Los numeros son consecutivos.')
    else:
        print('Error ...')
else:
    print('Error ...')

print('\nProceso terminado')