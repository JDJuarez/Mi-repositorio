#Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo, 2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, mostrar un mensaje de error.

import os

os.system('cls')

n = int(input('Dame un numero entero entre 1 y 7: \n'))

if n >= 1 and n <= 7:
    print(f'El día de la semana correspondiente es ---> ', end='')
    if n == 1:
        print("Domingo")
    elif n == 2:
        print("Lunes")
    elif n == 3:
        print("Martes")
    elif n == 4:
        print("Miercoles")
    elif n == 5:
        print("Jueves")
    elif n == 6:
        print("Viernes")
    else:
        print("Sabado")
else:
    print('\nError ...')


print('\nProceso terminado')