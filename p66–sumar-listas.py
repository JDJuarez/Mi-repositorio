# Planteamiento del problema
# - Leer dos listas de n números
# - Sumar ambas listas y guardar el resultado en una tercer lista
# - Mostrar las tres listas
a = []
b = []
c = []

n = int(input('Cuantos elementos ?'))

print('Dame los elementos de la Lista 1: ')
for i in range(n):
    x = int(input(f'Lista 1 elemento {i}: '))
    a.append(x)
print(a)

print('Dame los elementos de la Lista 2: ')
for i in range(n):
    x = int(input(f'Lista 1 elemento {i}: '))
    b.append(x)
print(b)

print('Calculando la suma de la Lista 1 + Lista 2')
for i in range(n):
    x = a[i] + b[i]
    c.append(x)
print(c)