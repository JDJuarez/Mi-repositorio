#Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor final. El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system('cls')

    print('La temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario.')
    i = int(input('\nIntroduce la temperatura inicial i ? '))
    f = int(input('Introduce la temperatura final   f ? '))
    t = i
    print('\n\tTabla de temperatura:')
    print(f'Centigrados (°C)\tFarenheit (°F)')
    while t <= f:
        print(f'\t{t}°C\t\t   {float((t * 9/5) + 32)}')
        t += 1
    res = input('\nDeseas continuar (S/N) ? ')
    if res.upper()=='N':
        break

print('\nProceso terminado ...')