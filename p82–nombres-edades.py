import os
os.system('cls')
datos = {}

while True:
    nombre = input('Nombre ? ')
    if nombre!='':
        datos[nombre] = int(input('Edad ? '))
    else:
        break

print(datos, len(datos))

s=0
for n,e in datos.items():
    print(f'{n:<20} - {e:2}')
    s = s + e

print()
print(s)
print(s/len(datos))