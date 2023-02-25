# Se desea calcular el volumen de un cilindro dado su radio y altura, usando la siguiente formula: 
# Volumen = PI * (Radio * Radio) * Altura

import math
import os

os.system('cls')
print('Dame el valor del radio seguido de la altura del cilindro separados por un espacio:\n')
Radio, Altura = input().split()
Radio, Altura = [float(Radio), float(Altura)]

Volumen = 3.1416 * (Radio * Radio) * Altura
print(f'El volumen del cilindro es: {Volumen} ')