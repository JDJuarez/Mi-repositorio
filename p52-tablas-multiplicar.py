
n = int(input('Hasta que tabla quieres ?'))
m = int(input('Hasta dónde             ?'))

for i in range(1,n+1):
    print(f'\nTabla del {i}')
    for j in range(1,m+1):
        print(f'{i} x {j} = {i*j}')