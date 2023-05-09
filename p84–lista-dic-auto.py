import os
os.system('cls')

autos = [ 
    { 'marca':'Ford', 'modelo':'Mustang', 'ano': 1964 },
    { 'marca':'VW', 'modelo':'Jetta', 'ano': 2015 }
]

autos.append({'marca':'Ford','modelo':'focus','ano':2000})

print(autos, len(autos))

for auto in autos:
    print(auto)

print('\nDatos en forma de tabla')
for k in autos[0].keys(): #titulos de la tabla (los nombres de las columnas)
    print(f'{k}\t', end='')
print('\r')

for auto in autos: #Para cada auto en la lista de autos
    for v in auto.values(): #Para cada valor de cada columna en ese auto
        print(f'{v}\t', end='')
    print('\r')

print('\nDatos en forma de registros:')
for auto in autos:
    for k,v in auto.items():
        print(f'{k} - {v}')
    print('\r')