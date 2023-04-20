# Planteamiento del problema
# - El usuario captura n calificaciones entre 0 y 10, usa 99 para parar.
# - Se calculan y muestran:
# - Las calificaciones capturados
# - El numero de calificaciones capturados
# - La suma de las calificaciones
# - El promedio de las calificaciones
# - Cuantas calificaciones son mayores que el promedio y cuales son
# - La calificación mayor
# - La calificación menor

nums = []
n = 0
suma = 0
promedio = 0

while n!=99:
    n = float(input('Numero > '))
    if n>=0 and n<=10:
        nums.append(n)
        suma = suma + n
    else:
        print('x')

print('< fin')

promedio = suma / len(nums)

print('Se capturaron   : ', len(nums))
print('Los números son : ', nums)
print('\nEstadisticas:')
print('Suma    : ', suma)
print('Promedio: ', promedio)
print('Mayor   : ', max(nums))
print('Menor   : ', min(nums))

mp = []
for n in nums:
    if n > promedio:
        mp.append(n)

print('Mayores que promedio: ', len(mp))
print('Y son: ', mp)