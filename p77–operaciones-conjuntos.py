# Conjuntos 
c1 = {1, 2, 3, 4, 5}
c2 = {5,6,7,8,9,10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print(c1, c2, c3, c4, '\n')

# Unión de conjuntos
print(c1.union(c2), '\n')
print(c1 | c3, '\n')

# Intersección de conjuntos
print(c1.intersection(c2), '\n')
print(c2 & c3, '\n')

# Diferencia de conjuntos
print(c1.difference(c2), '\n')
print(c2 - c3, '\n')

# Diferencia simétrica de conjuntos
print(c1.symmetric_difference(c2), '\n')
print(c2 ^ c3, '\n')

# Si es subconjunto
print(c4.issubset(c1), '\n')
print(c3 <= c2 , '\n')

# SuperConjunto, Comprobar conjunto mayor
print(c1.issuperset(c4), '\n')
print(c2 >= c3, '\n')

# Saber si un elemento esta en un conjunto
print(2 in c1, '\n')
print(6 not in c1, '\n')