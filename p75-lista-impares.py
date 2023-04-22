# - Llenar un lista con los primeros n números impares (ej 1 3 5 7 9 11 n)
# - Calcular e imprimir la suma y promedio de los números
# - Mostrar los números que son divisibles entre 3 y sumarlos
# - Pedir un elemento a buscar en la lista original y decir si esta y en que posición

import os

os.system('cls')

impares = []
imparesDivisiblesENTres = []
nImpar = 0
suma = 0
suma2 = 0
promedio = 0

n = int(input('Numeros impares ? '))

while len(impares) != n:
    nImpar = nImpar + 1
    if(nImpar%2 != 0):
        impares.append(nImpar)
        suma = suma + nImpar
print(impares)
promedio = suma/len(impares)
print(f'\nSuma    : {suma}')
print(f'Promedio: {promedio}')

for  i in impares:
    if (i%3 == 0):
        imparesDivisiblesENTres.append(i)
        suma2 = suma2 + i

print(f'\nNúmeros que son divisibles entre 3: ')
print(f'{imparesDivisiblesENTres}')
print(f'Suma ---> {suma2}')

while True:
    elemento = int(input('\nElemento a buscar en la lista original (Salir "0") --> ? '))
    if elemento in impares:
        # print(f'está en la lista, posicion es {impares.index(elemento)}')
        # indice = mi_lista.index(3)
        print(f'El número {elemento} está en la posición {impares.index(elemento)} de la lista original.')
    elif(elemento == 0):
        break
    else:
        print('No está en la lista.')
print('\nProceso terminado ...')