#Convertir una temperatura de grados Celcius a grados Farenheit y viceversa

import os

os.system('cls')
print('Convertir una temperatura de grados Celcius a grados Farenheit y viceversa\n')
opcion = input('[C]elcius [F]arenheit ? ').upper()

if opcion == 'C':
    print('\nConvertir a Celcius')
    temp = float(input('Dame grados Farenheit ? '))
    res = (temp-32)*5/9
    print(f'{temp} grados Farenheit, equivale a {res} grados Celcius')
else:
    print('\nConvertir a Farenheit')
    temp = float(input('Dame grados Celcius ? '))
    res = (temp*9/5)+32
    print(f'{temp} grados Celcius, equivale a {res} grados Farenheit')
