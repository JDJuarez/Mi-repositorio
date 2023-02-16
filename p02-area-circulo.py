# Calcular el area de un circulo
import math

#Entrada
print('Calculando el area de un circulo:\n')
radio = float(input('Dame el radio: '))

#Proceso
area = math.pi * math.pow(radio,2)

#Salida
print(f'El circulo de radio {radio} tiene un area de {area}')