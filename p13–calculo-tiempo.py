# Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos, considerando que:
# 1 día tiene 24 horas, 
# 1 hora tiene 60 minutos, 
# 1 minuto tiene 60 segundos.

import math
import os

os.system('cls')
horas = float(input('Dame la cantidad en horas:\n'))

dias = horas/24
minutos = horas * 60
segundos = horas * 60 * 60

print(f'La cantidad de {horas} convertidas son:\n')
print(f'\nDias ------> {dias}\n')
print(f'\Minutos ----> {minutos}\n')
print(f'\nSegundos --> {segundos}\n')