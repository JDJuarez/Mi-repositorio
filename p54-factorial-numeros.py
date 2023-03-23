#Imprime el factorial de un número, desde 1 hasta n

n = int(input('Dame un número ? '))

for i in range(1, n+1):
    f = 1
    print(f'{i}!=', end='')
    for j in range(1, i+1):
        print(f'{j}', end= ' ')
        if j != i:
            print(f'x', end= ' ')
        f = f * j
    print(f' = {f}')