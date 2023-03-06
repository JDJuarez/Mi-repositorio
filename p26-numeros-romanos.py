#Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V, VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error.

import os

os.system('cls')

n = int(input('Dame un número entre 1 y 10: \n'))

if n >= 1 and n <= 10:
    print(f'Su equivalente en número romano es ---> ', end='')
    if n == 1:
        print("I")
    elif n == 2:
        print("II")
    elif n == 3:
        print("III")
    elif n == 4:
        print("IV")
    elif n == 5:
        print("V")
    elif n == 6:
        print("VI")
    elif n == 7:
        print("VII")
    elif n == 8:
        print("VIII")
    elif n == 9:
        print("IV")
    else:
        print("X")
else:
    print('\nError ...')


print('\nProceso terminado')