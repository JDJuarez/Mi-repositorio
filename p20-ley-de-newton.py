# Calcula la segunda ley de newton (fuerza, masa, aceleración)
import os

os.system('cls')
print('Calcular la segunda ley de newton (fuerza, masa, aceleración\n)')
print('[F] uerza            (f = m * a)')
print('[M] asa              (m = f / a)')
print('[A] celeración       (a = f / m)')
op = input('Elige opción ? ').upper()

if op=='F':
    print('\nCalculando la fuerza ...')
    m = int(input('Dame la masa        ? '))
    a = int(input('Dame la aceleración ? '))
    f = m * a 
    print(f'\nLa fuerza es {f}')
elif op == 'M':
    print('\nCalculando la Masa ...')
    f = int(input('Dame la fuerza ? '))
    a = int(input('Dame la aceleración ? '))
    m = f / a
    print(f'\nLa masa es {m}')
elif op == 'A':
    print('\nCalculando la aceleración')
    print(f'\nCalculando la aceleración ...')
    f = int(input('Dame la fuerza ? '))
    m = int(input('Dame la masa ? '))
    a = f / m
    print(f'\nLa aceleración es {a}')
else:
    print('\nOpción inválida')

print('\nProceso terminado ...')