# - Leer dos listas con 5 elementos
# - Multiplica las listas y guárdalos en una tercera lista
# - Imprime las tres listas

a = []
b = []
c = []

print('Dame los elementos de la Lista 1: ')
for i in range(5):
    x = int(input(f'Lista 1 elemento {i + 1}: '))
    a.append(x)
print(a)

print('Dame los elementos de la Lista 2: ')
for i in range(5):
    x = int(input(f'Lista 1 elemento {i + 1}: '))
    b.append(x)
print(b)

print('Calculando multiplicación de la Lista 1 * Lista 2: ')
for i in range(5):
    x = a[i] * b[i]
    c.append(x)
print(c)