# - Leer n notas hasta introducir un 0
# - Las notas pueden estar entre 0 y 100 (validar)
# - Imprime: 
#   - cuantas notas, las notas, 
#   - suma, promedio, 
#   - notas menores al promedio y cuantas son
#   - nota máxima y nota mínima

Notas = []
n = 1
suma = 0
promedio = 0

while n!=0:
    n = float(input('Notas --> '))
    if n>0 and n<100:
        Notas.append(n)
        suma = suma + n
    elif n!=0:
        print('La nota no esta entre 0 y 100')

print(f'-'*12)

promedio = suma / len(Notas)

print(f'Se capturaron: {len(Notas)} notas')
print(f'Las notas son: {Notas}')
print('\nEstadisticas:')
print(f'Suma: {suma}')
print(f'Promedio: {promedio}')

mp = []
for n in Notas:
    if n < promedio:
        mp.append(n)

print('Menores que promedio: ', len(mp))
print('Y son: ', mp)

print('Mayor: ', max(Notas))
print('Menor: ', min(Notas))

print('\nProceso terminado ...')