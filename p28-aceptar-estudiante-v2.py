#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La 
#Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.

import os

os.system('cls')
print('Aceptar un estudiante en base a su edad, sexo y sus calificaciones: \n')
nombre = input('Dame tu nombre ? ')
calificaciones = float(input('Ingresa tu promedio de calificaciones ? '))

if calificaciones > 8 and calificaciones < 9.5:
    edad = int(input('Dame tu edad ? '))
    
    if edad > 21:
        print('Sexo: ? ')
        print('(h) ombre: ? ')
        print('(m) ujer: ? ')
        sexo = input().upper()

        if sexo == 'M':
            print(f'\n{nombre} bienvenida a la Universidad, tu edad es {edad} años y tu promedio de calificaniones {calificaciones} lo permite.')
        else: 
            print('Aceptamos solo a mujeres ...')
    else:
        print('Aceptamos solo mayores de 21 años ...')
else:
    print('No aceptamos calificaciones que no esten entre 8 y 9.5 ...')

print('\nProceso terminado')