# Se desea llevar el control de la inscripción a un evento académico de la 
# Universidad Patito. Se especifica: Tipo de usuario, paquete y cantidad.

# - Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
# - Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales 
#   $800, [3] Con kit de acceso $900

# Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario 
# más el precio de tipo de paquete, y multiplicando por la cantidad solicitada.

# Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de 
# acuerdo a lo siguiente

# - Es Alumno 20%
# - Es Trabajador y un 10%
# - Es Docente y un 5%

# Al final mostrar un resumen con los datos calculados de la venta.
# Al terminar de procesar las ventas mostrar el total de ventas del día:
import os
importeTotal = float(0)
while(True):
    os.system('cls')
    print('-'*46)
    print('-'*46)
    print('        Universidad Patio SA de CV         ')
    print('Sistema de Inscripción Congreso de Sistemas\n')

    tu = int(input('Tipo de usuario: [1] Alumno      $100\n\t\t [2] Trabajador  $200\n\t\t [3] Docente     $500\n\n\t\t ? '))
    
    if tu == 1:
        usuario = 'Alumno'
        u = 100
        d = 20
    elif tu == 2:
        usuario = 'Trabajador'
        u = 200
        d = 10
    else:
        usuario = 'Docente'
        u = 500
        d = 5

    tp = int(input('\nTipo de paquete: [1] Solo conferencias $600\n\t\t [2] Con eventos sociales $800\n\t\t [3] Con kit de acceso $900\n\n\t\t ? '))

    if tp == 1:
        paquete = 'Solo conferencias'
        p = 600
    elif tp == 2:
        paquete = 'Con eventos sociales'
        p = 800
    else:
        paquete = 'Con kit de acceso'
        p = 900
    
    c = int(input('\nCantidad:\t ? '))
    subtotal = (u + p) * c
    descuento = float(subtotal * d)/100
    total = float(subtotal - descuento)

    importeTotal = importeTotal + total

    print('\n')
    print('-'*46)
    print(f'\nTu pedido fue: \t \t{c}\nTipo de usuario: \t{usuario}\nTipo de paquete: \t{paquete}')

    print(f'\nSubtotal:\t\t${subtotal} \nDescuento de ({d}%):\t${descuento}\nTotal de:\t\t${total}')
    print('\n')
    print('-'*46)
    bandera = True
    while(bandera == 1):
        print('\nDeseas continuar (S/N) ? ', end= ' ')
        res = input()
        if res.upper() == 'S' or res.upper() == 'N':
            bandera = False
    if res.upper()=='N':
            break
print('\n')
print('-'*46)
print('\n')
print(f'Importe Total de la Venta: ${importeTotal:.2f}')
print('\n')
print('\nProceso terminado ...')
print('\n')
print('-'*46)