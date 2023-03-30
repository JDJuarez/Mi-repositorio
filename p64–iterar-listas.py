# Iterar sobre los elementos de la lista
import os
os.system('cls')

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print(f'Todos los elementos:\n {nums}')

print(f'nIterar por los elemtos de la lista forma 1:')
for n in nums: 
    print(n, end=' ')

print('\nIterar por los elemtos de la lista forma 2:')
for i in range(len(nums)):
    print(nums[i], end=' ')
print('\nMostar cada elemto de la lista sumado en 2:')
for n in nums: 
    print(n+2, end=' ')
print(f'\n{nums}')
print('\nModificar la lista sumando 10 a cada elemento:')
for i in range(len(nums)):
    nums[i] = nums[i] + 10
print(f'\n{nums}')
