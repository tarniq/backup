import os
os.system('cls')


def soma (x, y, z):
    if z is not None:
        print(f'{x=}, {y=}, {z=}', '|', f'o resultado da soma de {x} + {y} + {z} é igual a = {x+y+z}')
    else:
        print(f'{x=}, {y=}', '|', f'o resultado da soma de {x} + {y} é igual a = {x+y}')

x = int(input('digite um numero: '))
y = int(input('digite um numero: '))
z = int(input('digite um numero: '))

soma(x,y,z)  

soma(x=5,y=4,z=3) 
soma(x=6,y=7,z=7) 
soma(x=9,y=4,z=23) 
