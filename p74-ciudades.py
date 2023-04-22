# - Leer n nombres de ciudades en una lista hasta introducir $
# - Imprimir cuantos elementos son, y la lista completa
# - Ordenar la lista en orden descendente y mostrar (sort)
# - Imprimir cuantas ciudades inician con la letra consonante (startswith) y sus nombres

import os

os.system('cls')

ciudades = []
ciudad = ''
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
ciudadesInicianConConsonante = []

while ciudad!='$':
    ciudad = input('Introduce nombre de ciudad: ')
    if(ciudad !='$'):
        ciudades.append(ciudad)

print(f'\nSon ---> {len(ciudades)} ciudades')

print(f'\nLas ciudades son: ')
print(f'{ciudades}')

print('\nOrdenadas (sort): ')
ciudades.sort()
print(ciudades)
print('En orden descendente: ')
ciudades.sort(reverse=True)
print(ciudades)

for isConsonante in ciudades:

    if(isConsonante.lower().startswith(tuple(consonantes))):
        ciudadesInicianConConsonante.append(isConsonante)

print(f'\nCiudades que inician con consonante son ---> {len(ciudadesInicianConConsonante)}')
print(f'{ciudadesInicianConConsonante}')