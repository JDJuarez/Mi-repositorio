# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte
# Mostrar los dígitos individuales y el número de la suerte.

import math
import os

os.system('cls')
anio = int(input('Dame el año de nacimiento: '))

unidadesDeMil = anio //1000
centenas = ( anio - (unidadesDeMil * 1000) ) // 100
decenas = ( anio - (unidadesDeMil * 1000) - (centenas * 100) ) // 10
unidades = anio - centenas*100 - unidadesDeMil*1000 - decenas*10

print('Los digitos individuales son:')
print('Unidades de mil -> ', unidadesDeMil)
print('Centenas -> ', centenas)
print('Decebas -> ', decenas)
print('Unidades -> ', unidades)

numeroDeLaSuerte = unidadesDeMil + centenas + decenas + unidades

print(f'\nEl número de la suerte es: {numeroDeLaSuerte}')