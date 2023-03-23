#Imprimir el factorial de un número

n = int(input('Dame un número ? '))

f = 1

for i in range(1, n+1):
    print(f'{i}', end=' x ')
    f = f * i

print(f'\nEl factorial es {f}')