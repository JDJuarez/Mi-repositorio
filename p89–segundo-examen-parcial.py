import os
os.system('cls')

empleados = [
    {'nombre':'Carlos', 'edad':45, 'sexo (h/m)':'h','sueldo':7000},
    {'nombre':'Rocio', 'edad':35, 'sexo (h/m)':'m','sueldo':7000},
    {'nombre':'Ana', 'edad':35, 'sexo (h/m)':'M','sueldo':7000},
]

print('\nMuebleria Muebles Dico')
print('Sistema de Procesamiento de Empledos')
print('\nCaptura de datos de los empleados * o enter para terminar:')


while True:
    empleado = {}
    nombre = input('\nnombre\t\t? ')
    if nombre == '' or nombre == '*':
        break
    else:
        empleado['nombre'] = nombre
        empleado['edad'] = int(input('edad\t\t? '))
        
        while True:
            sexo = input('sexo (h/m)\t? ').upper()
            if sexo == 'H' or sexo == 'M':
                empleado['sexo (h/m)'] = sexo
                break
            else:
                print('\nEscribiste mal, para:')
                print('hombre ---> h')
                print('mujer  ---> m:')
                print('')                 

        empleado['sueldo'] = int(input('sueldo\t\t? $'))
        empleados.append(empleado)

print('\nLos datos como se guardan:')
print('')
print(empleados)

print('\nTabla de datos: ')
print("Nombre\tEdad\tSexo\tSalario") #titulos de la tabla (los nombres de las columnas)

for empleado in empleados: # para cada empleado en la lista de empleados
    for j in empleado.keys(): #para cada valor de cada empleado
        if j != 'sueldo':
            print(f'{empleado[j]}\t', end= '')
        else:
            print(f'{format(empleado[j],",.2f")}\t', end= '')
    print('\r')

# # calcular suma de mujeres
smujeres = 0
for k in empleados:
    if k['sexo (h/m)'] == 'm' or k['sexo (h/m)'] == 'M':
        smujeres = smujeres + 1

# # calcular suma de hombres
shombres = 0
for l in empleados:
    if l['sexo (h/m)'] == 'h' or l['sexo (h/m)'] == 'H':
        shombres = shombres + 1

# # calcular suma y promedio de Edad
sEdad = 0
pEdad = 0
for n in empleados:
    sEdad = sEdad + n['edad']
pEdad = sEdad/len(empleados)

# # calcular suma y promedio de Sueldos
sSueldos = 0
pSueldos = 0
for o in empleados:
    sSueldos = sSueldos + o['sueldo']
pSueldos = sSueldos/len(empleados)

print('\nResumen  : ')
print(f'Empleados: {len(empleados)}')
print(f'Mujeres  : {smujeres}')
print(f'Hombres  : {shombres}')
print(f'Edad     : suma:\t{sEdad},\t\tpromedio: \t{pEdad}')
print(f'Sueldo   : suma:\t{format(sSueldos,",.2f")},\tpromedio:\t{format(pSueldos,",.2f")}')
# Resumen: 
# Empleados : 4
# Mujeres : 2
# Hombres : 2
# Edad: suma : 124, promedio: 31.0
# Sueldo: suma: 9,700.00, promedio: 2,425.00