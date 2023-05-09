import os
os.system('cls')

grupo = [
    {'nombre':'Carlos', 'edad':45, 'carrera':'sistemas','promedio':9.0},
    {'nombre':'Rocio', 'edad':35, 'carrera':'contabilidad','promedio':10.0},
]

print(grupo, len(grupo))

while True:
    datos = {}
    nombre = input('\nnombre:')
    if nombre == '':
        break
    else:
        datos['nombre'] = nombre
        datos['edad'] = int(input('edad:'))
        datos['carrera'] = input('carrera:')
        datos['promedio'] = float(input('promedio:'))
        grupo.append(datos)

print(grupo, len(grupo))

print('\nDatos en forma de tabla')
for k in grupo[0].keys(): #titulos de la tabla (los nombres de las columnas)
    print(f'{k}\t', end='')
print('\r')

for alumno in grupo: # para cada auto en la lista de autos
    for v in alumno.values(): #para cada valor de cada columna en se auto
        print(f'{v}\t', end= '')
print('\r')

# calcular suma de edades
s = 0
sp = 0
for alumno in grupo:
    s = s + alumno['edad']
    sp = sp + alumno['promedio']
p = s / len(grupo)
pp = sp / len(grupo)

print('\nResumen:')
print(f'Edad:  suma {s}, promedio {p}')
print(f'Promedio: suma {sp}, promedio {pp}')