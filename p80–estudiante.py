import os
os.system('cls')

estudiante = {
    'nombre':'Juan Perez',
    'edad':45,
    'email':'jperez@msn.com',
    'Carrera':'Sistemas'
}

print(estudiante, len(estudiante),'\n')
estudiante['Calificación'] = 9.5

print(estudiante, len(estudiante),'\n')
estudiante['email'] = 'juanp@gmail.com'

print(estudiante, len(estudiante),'\n')
estudiante.update({'Sexo':'nombre','Semestre':7})

print(estudiante, len(estudiante), '\n')

for k in estudiante.keys():
    print(k)
print()
for v in estudiante.values():
    print(v)
print()
for k, v in estudiante.items():
    print(k, v)