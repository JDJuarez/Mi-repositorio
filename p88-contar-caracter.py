import os
os.system('cls')

aparicionesCaracter = {}

palabra = input('Cadena de caracteres ? ')

for i in palabra:
    if i in aparicionesCaracter:
        aparicionesCaracter[i] = 1 + aparicionesCaracter[i]
    else:
        aparicionesCaracter[i] = 1

print(f'{aparicionesCaracter}')