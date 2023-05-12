import os
os.system('cls')

numerosRomanos = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X', 11:'XI', 12:'XII', 13:'XIII', 14:'XIV', 15:'XV', 16:'XVI', 17:'XVII', 18:'XVIII', 19:'XIX', 20:'XX'}

while True:
    numeroRomano = int(input('Un número en arabigo entre 1 y 20 ? '))
    if numeroRomano > 0 and numeroRomano < 21:
        print(f'Su correspondiente número romano ---> {numerosRomanos[numeroRomano]}')
        break
    else:
        print('Error')