#Aceptar un estudienate en base a su edad y sus calificaciones

import os

os.system('cls')
print('Aceptar un estudiante en base a su edad y sus calificaciones: \n')
nombre = input('Dame tu nombre ? ')
edad = int(input('Dame tu edad ? '))

if edad >= 18:
    print('Dame dos calificaciones separadas por Enter ?')
    c1, c2 = int(input()), int(input())
    if c1>=8 and c2>=8:
        print(f'{nombre} bienvenido a la Universidad, tu edad es {edad} y tus califciaciones son {c1} y {c2} lo permiten')
    else:
        print('No aceptamos calificaciones menores de 8')
else:
    print('No aceptamos menores de edad ...')

print('\nProceso terminado')
    

print('\nProceso terminado')