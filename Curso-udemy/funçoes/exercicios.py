import re
import sys
def mutiplicacao(*args):
    total = 1
    for i in args:
        total *= int(i)
    return(total)
def validaçao(numeros_u):
    
    tupla_num = tuple(re.sub(r'[^0-9]',"", numeros_u))
    return(tupla_num)






numeros_u = input("Digite os nuemros que deseja multiplicar entre si: ")

numeros_p = validaçao(numeros_u)

if numeros_p == ():
    print("voce nao digitou numeros")
    sys.exit()

resultado = mutiplicacao(*numeros_p)
print(resultado)
