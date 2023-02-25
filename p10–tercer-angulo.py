# Dados dos ángulos de un triángulo, calcular el 3er ángulo, usando la siguiente formula: 
# angulo3 = 180 – (angulo1 + angulo2)

import math
import os

os.system('cls')
print('Dame el valor de los dos ángulos de un triángulo separados por un espacio:\n')
angulo1, angulo2 = input().split()
angulo1, angulo2 = [float(angulo1), float(angulo2)]

angulo3 = 180 - (angulo1 + angulo2)
print(f'El tercer angulo del triangulo es: {angulo3} ')