# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit, usando la siguiente formula:
# farenheit = (celcius × 9/5) + 32

import math
import os

os.system('cls')
celcius = float(input('Dame la temperatura en grados celcius:\n'))

farenheit = (celcius * 9/5) + 32
print(f'La temperatura en grados farenheit es: {farenheit} ')