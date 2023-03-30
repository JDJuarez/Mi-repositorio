# Acceder a los elementos de una lista
import os
os.system('cls')
nums = [10, 20, 30, 40, 60, 70, 10, 20, 99,100]

print(type(nums))
print(f'Tamaño de la lista {len(nums)}')
print(f'Todos los números {nums}')
print(f'El primero y el último {nums[0]}, {nums[-1]}')
print(f'Del 30 al 70 {nums[2:6]} \n')
print(f'Tres primeros {nums[:3]} \n')
print(f'Tres últimos {nums[7:]} \n')
