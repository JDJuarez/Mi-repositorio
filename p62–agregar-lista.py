# Agregar elementos a la lista 
import os
os.system('cls')

nums = [80.3, 12.5, 60.2, 30.4]
print(f'Todos los números :\n {nums} - {len(nums)}')
nums.append(90)
nums.append(100)
print(f'Agregar al final de la lista:\n {nums}')
nums.insert(5,80)
print(f'Insertar número:\n {nums}')
nums.extend([110,120,130])
print(f'Extender la lista con más elementos:\n {nums}')