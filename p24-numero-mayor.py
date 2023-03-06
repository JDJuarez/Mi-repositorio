#Dados tres números enteros, verificar cual es el mayor.

import os

os.system('cls')
print('Dame tres números enteros separados con un espacio: \n')
n1, n2, n3 = input().split()
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n1 > n2:
    print(f'El numero mayor es ', end='')
    if n1 > n3:
        print(n1)
elif n2 > n3:
    print(f'El numero mayor es ', end='')
    print(n2)
elif n3 > n2:
    print(f'El numero mayor es ', end='')
    print(n3)
elif n2 == n3:
    print('Son iguales los numeros.')

print('\nProceso terminado')