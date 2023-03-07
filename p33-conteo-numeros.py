# Cuenta números, la suma, cuenta positivos, cuenta negativos y ceros, hasta salir con 999

import os

os.system('cls')

cuenta = 0
suma = 0
cp = cn = cz = 0
print('Cuenta números, la suma, cuenta positivos, cuenta negativos y ceros, hasta salir con 999\n')

while True:
    num = int(input('Número ? '))
    if num != 999:
        cuenta = cuenta + 1
        suma = suma + num
        if num > 0:
            cp = cp + 1
        elif num < 0:
            cn = cn + 1
        else:
            cz = cz + 1
    else:
        break

print('\nResumen:\n')
print(f'Se capturaron : {cuenta} números')
print(f'La suma es : {suma}')
print(f'El promedio es  : {suma / cuenta}')
print(f'Positivos : {cp}\nNegativos: {cn}\nCeros {cz}')