# p69-listas-aleatorios (1)
# Planteamiento del problema
# - Generar dos listas de 10 números aleatorios cada una y mostrarlas
# - Elevar cada elemento de las listas al cuadrado
# - Generar una tercer lista con la suma de las otras dos listas 
# - Imprimir las tres listas

import random

a = []
b = []
c = []

print('Generando listas de numeros aleatorios ...')

for n in range(10):
    a.append(random.randint(5,10))
    b.append(random.randint(5,10))

print(a)
print(b)

for n in range(10):
    a[n] = a[n] * a[n]
    b[n] = b[n] * b[n]

print(a)
print(b)

for n in range(10):
    c.append(a[n] + b[n])

print(c)