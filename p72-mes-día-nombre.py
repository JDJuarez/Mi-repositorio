# - Leer un número de mes (ej 4).
# - Imprimir: días del mes, y nombre del mes (ej marzo, 30).
# - Asume 28 para febrero, guarda días en una lista, y nombres de mes en otra.

pos = 0
mes = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    pos = int(input('Dame un mes entre 1 y 12 ---> ? '))
    if pos>=1 and pos<=12:
        break
    else:
        print('No es un mes')

print(f'Elegiste el mes --> ({mes[pos-1]},{dias[pos-1]})')