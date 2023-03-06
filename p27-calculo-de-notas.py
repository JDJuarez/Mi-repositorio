# Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir un mensaje de acuerdo al promedio obtenido:

# >0 y <= 6 Quedas reprobado
# >6 a <=7 Pasas de panzazo
# >7 y <=8 Muy bien, pues mejorar
# >8 y <=9 Excelente sigue así
# >9 y <=10 Perfecto tu esfuerzo valió la pena

import os

os.system('cls')
print('Para calcular el promedio de 5 calificaciones y evaluar el resultado. \n')

print('Dame 5 calificaciones separadas con un espacio:')
c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = [int(c1), int(c2), int(c3), int(c4), int(c5)]

promedio = (c1 + c2 + c3 + c4 + c5) / 5

print(f'\nEl promedio es {promedio} --> ', end='')

if(promedio > 0 and promedio <= 6):
    print('Quedas reprobado.')
if(promedio > 6 and promedio <= 7):
    print('Pasas de panzazo.')
if(promedio > 7 and promedio <= 8):
    print('Muy bien, pues mejorar.')
if(promedio > 8 and promedio <= 9):
    print('Excelente sigue así.')
if(promedio > 9 and promedio <= 10):
    print('Perfecto tu esfuerzo valió la pena.')

print('\nProceso terminado')