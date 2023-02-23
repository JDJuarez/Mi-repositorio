#Efectua operaciones matemáticas con dos números

print('Efectua operaciones matemáticas con dos números')
print('Dame dos valores separados por espacio:')
x, y = input().split()
x, y = [float(x), float(y)]

suma = x + y
resta = x -y
mult = x * y
div = x / y
dive = x // y
res = x % y
exp = x ** y

print(f"Suma: {suma}\nRes: {resta}\nMultiplicación: {mult}")
print(f"División: {div}\nDiv Entera: {dive}\nResiduo: {res}")
print(f"Exponenciación: {exp}")