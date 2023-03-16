#Suma y promedio de n números introducidos por el usuario
import os
os.system('cls')

n = int(input('Cuantos números ? '))

s=0
for x in range(1, n+1):
    print(f'Número {x}: ', end=' ')
    num = float(input())
    s += num

print(f'\nSuma {s} y el promedio es {s/n:.2f}')