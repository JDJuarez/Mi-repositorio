#Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados, usando la siguiente formula:

import math

print('Divide un número de 3 cifras en centenas, decenas, unidades:\n')
longlado1 = float(input('Dame lo que mide el primer lado del triangulo:\n'))
lognlado2 = float(input('Dame lo que mide el Segundo lado del triangulo:\n'))

hipotenusa = math.sqrt((lognlado1 * lognlado1)+(lognlado2 * lognlado2))
print(f'La hipotesusa del triangulo es: {hipotenusa} ')