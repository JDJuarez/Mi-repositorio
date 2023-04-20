# Planteamiento del problema
# - El usuario introduce una serie de nombres, junto con sus edades, hasta que se 
# introduce *.
# - Se desea mostrar 
# - alumnos mayores de edad: sus edades y sus nombres.
# - el alumno con la mayor edad: su edad y su nombre.

nombres = []
edades = []
i = 0
pos = 0
may = 0

print('Introduce nombre y edades * para terminar:\n')

while True:
    nombre = input('Nombre: ')
    if nombre == '*':
        break
    else:
        nombres.append(nombre)
        edad = int(input('Edad: '))
        edades.append(edad)

print(nombres)
print(edades)

for i in range(len(nombres)):
    if edades[i] >=18:
        print(f'Nombre: {nombres[i]}, Edad: {edades[i]}')

may = max(edades)
pos = edades.index(may)

print('La persona de mayor edad es :')
print(f'Nombre: {nombres[pos]}, Edad: {edades[pos]}')