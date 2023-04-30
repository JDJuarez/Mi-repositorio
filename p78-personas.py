# Dados los siguientes nombres: 
# - Juan, Maria, Pedro, Jose, Rocio 
# - Pedro, Juan, Pablo, Mateo, Esther

import os
os.system('cls')

print('-'*30)
print('-'*30)
#Crea dos conjuntos uno para cada lista de nombres y muéstralos ( A, B )
A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'} 
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print(f'Conjunto A ---> {A}')
print(f'Conjunto B ---> {B}')

#Calcula y muestra:
print('\nUnion de los conjuntos ( A | B)')
print(A.union(B))
print('\nIntesección de los conjuntos ( A & B)')
print(A.intersection(B))  
print('\nDiferenia de los conjuntos ( A - B )')
print(A.difference(B)) 
print('\nDiferencia simetrica de los conjuntos ( A ^ B )')
print(A.symmetric_difference(B))

#Calcula y muestra también
print('\nSi el conjunto de nombres Pablo, Mateo, es subconjunto de B')
C = {'Pablo', 'Mateo'}
print(C.issubset(B))
print('\nSi el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica')
D = {'Reynaldo', 'Angelica'}
print(A.issuperset(D))
print('\nSi Pedro esta en A')
print('Pedro' in A)
print('\nSi Lilia no esta en B')
print('Lilia' not in B)