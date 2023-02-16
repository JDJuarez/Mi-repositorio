# Calcular la paga total de un trabajador

print('Calculando la paga de un trabajador\n')
nombre = input('Dame tu nombre: ')
horas = int(input('Horas trabajadas: ') )
paga = float(input('Paga por hora: ') )

tasa = 0.3

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
print('\nResumen de pagos: \n')
print(f'El trabajador {nombre} trabajo {horas} horas con una paga de {paga}, impuesto de {tasa}%')
print(f'Paga bruta: {pagabruta}')
print(f'Impuessto : {impuesto}')
print(f'Paga neta : {paganeta}')