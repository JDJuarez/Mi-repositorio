# Planteamiento del problema
# - El usuario teclea un día entre lunes y domingo
# - Se le presenta la paga que corresponde a ese día
# - Tanto días como paga están almacenados en dos listas
dia = ''
pos = 0
dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
paga = [100,200,300,400,500,600,700]

while True:
    dia = input('Dame un dia entre lunes y domingo ? ')
    if dia in dias:
        break

print('Elegiste el dia ',dia)
pos = dias.index(dia)

print('La paga es : ', paga[pos])