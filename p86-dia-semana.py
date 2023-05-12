import os
os.system('cls')

diasSemana = {1:'Domingo', 2:'Lunes', 3:'Martes', 4:'Miercoles', 5:'Jueves', 6:'Viernes', 7:'Sabado'}

while True:
    diaSemana = int(input('Un número de día ? '))
    if diaSemana > 0 and diaSemana < 8:
        print(f'Su correspondiente dia de semana es ---> {diasSemana[diaSemana]}')
        break
    else:
        print('Error')
