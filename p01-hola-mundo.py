# Lee datos y envia un saludo

#Entrada
print('Leyendo datos y enviando un saludo:\n')
nombre = input('Dame tu nombre ? ') # aqui se lee cadena
edad = int(input('Dame la edad ? '))
peso = float(input('Dame tu peso ? '))

#salida
print(f'{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}')
print(type(nombre)) #aqui se muestra el tipo de dato de una variable
print(type(edad))
print(type(peso))