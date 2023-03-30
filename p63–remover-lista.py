# Remover elementos de la lista
import os
os.system('cls')

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f'Todos los números:\n {nums} - {len(nums)}')
nums.remove(99)
print(f'Remover primera ocurrencia:\n {nums} - {len(nums)}')
num=nums.pop(8)
print(f'Remover elemto en una posición:\n {nums} - {num} - {len(nums)}')
num=nums.pop()
print(f'Remover el último elemento:\n {nums} - {num} - {len(nums)}')
nums.clear()
print(f'Remover todos:\n {nums} - {len(nums)}')