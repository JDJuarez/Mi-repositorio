import os
os.system('cls')
#Dados los siguientes números:
A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}
#Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)
print(f'Conjunto A ---> {A}')
print(f'Conjunto B ---> {B}')
print(f'Conjunto C ---> {C}')
#Calcula y muestra:
print('\nUnión de los conjuntos A y B ( A | B )')
print(A.union(B))
print('\nUnión de los conjuntos B y C ( B | C )')
print(B.union(C))
print('\nDiferencia de A y C ( A - C)')
print(A.difference(C))
print('\nDiferencia simétrica de B y C ( B ^ C)')
print(B.symmetric_difference(C))
print('\nIntersección de B y C ( B & C )')
print(B.intersection(C))

#Calcula y responda a las siguientes preguntas>'
print('\nA es subconjunto de B ? ')
print(A.issubset(B))
print('\nC es subconjunto de A ?' )
print(C.issubset(A))
print('\n 100 esta en A ? ')
print(100 in A)
print('\n60 esta en A , y en B y en C ? ')
print('60 en A ---> ', 60 in A)
print('60 en B ---> ', 60 in B)
print('60 en C ---> ', 60 in C)
print('\n 900 no esta en C ? ')
print(900 not in C)